import streamlit as st
import pandas as pd
import numpy as np
import re
import io
from datetime import datetime
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import PyPDF2
from docx import Document
import openai
from typing import Dict, List, Tuple, Any
import json
from deep_analysis_module import create_deep_analysis_dashboard
from critical_review_module import create_critical_review_dashboard
from technical_annex_analyzer import create_technical_annex_comprehensive_analysis_tab

# Configuration
st.set_page_config(
    page_title="COST 2025 Proposal Analyzer",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded"
)

class COSTAnalyzer:
    def __init__(self):
        self.openai_client = openai.OpenAI(api_key=st.secrets.get("OPENAI_API_KEY", ""))
        
        # COST 2025 Requirements Framework
        self.requirements = {
            "technical_format": {
                "max_pages": 15,
                "font": "Arial",
                "font_size": 10,
                "line_spacing": 1,
                "max_file_size_mb": 10,
                "format": "PDF",
                "anonymity_required": True
            },
            "evaluation_criteria": {
                "excellence": {
                    "weight": 0.33,
                    "threshold": 3.0,
                    "subcriteria": [
                        "scientific_innovation",
                        "technological_advancement", 
                        "networking_value",
                        "interdisciplinary_approach",
                        "open_science_commitment"
                    ]
                },
                "impact": {
                    "weight": 0.33,
                    "threshold": 3.0,
                    "subcriteria": [
                        "societal_impact",
                        "economic_impact",
                        "scientific_impact",
                        "stakeholder_engagement",
                        "sdg_contribution"
                    ]
                },
                "implementation": {
                    "weight": 0.34,
                    "threshold": 3.0,
                    "subcriteria": [
                        "project_management",
                        "timeline_realism",
                        "resource_allocation",
                        "leadership_capability",
                        "risk_management"
                    ]
                }
            },
            "network_requirements": {
                "min_countries": 7,
                "min_itc_percentage": 50,
                "itc_countries": [
                    "Bulgaria", "Croatia", "Cyprus", "Czech Republic", "Estonia",
                    "Hungary", "Latvia", "Lithuania", "Malta", "Poland", 
                    "Portugal", "Romania", "Slovakia", "Slovenia"
                ]
            },
            "content_structure": {
                "state_of_art": {"required": True, "weight": 0.15},
                "rationale_networking": {"required": True, "weight": 0.15},
                "critical_mass": {"required": True, "weight": 0.10},
                "impact_objectives": {"required": True, "weight": 0.20},
                "stakeholder_involvement": {"required": True, "weight": 0.15},
                "action_structure": {"required": True, "weight": 0.10},
                "work_plan": {"required": True, "weight": 0.10},
                "deliverables": {"required": True, "weight": 0.05}
            }
        }
        
        # Policy compliance requirements
        self.policy_requirements = {
            "inclusiveness": {
                "itc_participation_min": 50,
                "itc_leadership_min": 50,
                "geographic_balance": True
            },
            "gender_equality": {
                "female_participation_target": 50,
                "gender_equality_plan_required": True,
                "gear_tool_usage": True
            },
            "young_researchers": {
                "yri_participation_min": 50,
                "yri_leadership_allocation": 45,
                "mentorship_programs": True
            }
        }

    def extract_text_from_pdf(self, pdf_file) -> str:
        """Extract text from uploaded PDF file"""
        try:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text() + "\n"
            return text
        except Exception as e:
            st.error(f"Error reading PDF: {str(e)}")
            return ""

    def extract_text_from_docx(self, docx_file) -> str:
        """Extract text from uploaded DOCX file"""
        try:
            doc = Document(docx_file)
            text = ""
            for paragraph in doc.paragraphs:
                text += paragraph.text + "\n"
            return text
        except Exception as e:
            st.error(f"Error reading DOCX: {str(e)}")
            return ""

    def analyze_technical_compliance(self, file_content: str, file_size_mb: float) -> Dict:
        """Analyze technical format compliance"""
        compliance_score = 100
        issues = []
        
        # File size check
        if file_size_mb > self.requirements["technical_format"]["max_file_size_mb"]:
            compliance_score -= 20
            issues.append(f"File size ({file_size_mb:.1f}MB) exceeds 10MB limit")
        
        # Page count estimation (rough)
        estimated_pages = len(file_content.split()) / 300  # Approximate words per page
        if estimated_pages > self.requirements["technical_format"]["max_pages"]:
            compliance_score -= 30
            issues.append(f"Estimated {estimated_pages:.1f} pages exceeds 15-page limit")
        
        # Anonymity check
        anonymity_violations = self._check_anonymity(file_content)
        if anonymity_violations:
            compliance_score -= 25
            issues.extend(anonymity_violations)
        
        return {
            "score": max(0, compliance_score),
            "issues": issues,
            "estimated_pages": estimated_pages,
            "file_size_mb": file_size_mb
        }

    def _check_anonymity(self, text: str) -> List[str]:
        """Check for potential anonymity violations"""
        violations = []
        
        # Common patterns that might violate anonymity
        patterns = [
            (r"\b[A-Z][a-z]+ University\b", "University names detected"),
            (r"\bDr\. [A-Z][a-z]+\b", "Author names with titles detected"),
            (r"\bProf\. [A-Z][a-z]+\b", "Professor names detected"),
            (r"\b[A-Z][a-z]+ et al\.\b", "Author citations detected"),
            (r"\bour previous work\b", "Self-reference detected"),
            (r"\bwe have shown\b", "Self-reference detected"),
            (r"\bin our lab\b", "Lab reference detected")
        ]
        
        for pattern, message in patterns:
            if re.search(pattern, text, re.IGNORECASE):
                violations.append(message)
        
        return violations

    def analyze_content_quality(self, text: str) -> Dict:
        """Analyze content quality using AI"""
        if not self.openai_client.api_key:
            return {"error": "OpenAI API key not configured"}
        
        try:
            prompt = f"""
            Analyze this COST Action technical annex excerpt for quality across these dimensions:
            
            1. Scientific Excellence (0-5 scale)
            2. Innovation Level (0-5 scale)
            3. Networking Rationale (0-5 scale)
            4. Impact Potential (0-5 scale)
            5. Implementation Feasibility (0-5 scale)
            
            Text excerpt (first 2000 chars):
            {text[:2000]}
            
            Provide scores and brief justifications in JSON format:
            {{
                "scientific_excellence": {{"score": X, "justification": "..."}},
                "innovation": {{"score": X, "justification": "..."}},
                "networking": {{"score": X, "justification": "..."}},
                "impact": {{"score": X, "justification": "..."}},
                "implementation": {{"score": X, "justification": "..."}}
            }}
            """
            
            response = self.openai_client.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.1
            )
            
            result = json.loads(response.choices[0].message.content)
            return result
            
        except Exception as e:
            return {"error": f"AI analysis failed: {str(e)}"}

    def analyze_section_coverage(self, text: str) -> Dict:
        """Analyze coverage of required sections"""
        sections_found = {}
        
        section_keywords = {
            "state_of_art": ["state of the art", "current research", "background", "literature review"],
            "rationale_networking": ["networking", "collaboration", "rationale", "why network"],
            "critical_mass": ["critical mass", "network size", "participants", "consortium"],
            "impact_objectives": ["impact", "objectives", "goals", "outcomes"],
            "stakeholder_involvement": ["stakeholders", "industry", "policy", "end users"],
            "action_structure": ["structure", "organization", "management", "governance"],
            "work_plan": ["work plan", "tasks", "activities", "timeline"],
            "deliverables": ["deliverables", "outputs", "results", "products"]
        }
        
        for section, keywords in section_keywords.items():
            coverage_score = 0
            for keyword in keywords:
                matches = len(re.findall(keyword, text, re.IGNORECASE))
                coverage_score += min(matches * 10, 50)  # Cap at 50 per keyword
            
            sections_found[section] = {
                "coverage_score": min(coverage_score, 100),
                "weight": self.requirements["content_structure"][section]["weight"]
            }
        
        return sections_found

def create_compliance_dashboard(analyzer: COSTAnalyzer, analysis_results: Dict):
    """Create compliance visualization dashboard"""
    
    st.subheader("Technical Compliance Dashboard")
    
    # Technical compliance metrics
    tech_compliance = analysis_results.get("technical_compliance", {})
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            "Technical Compliance", 
            f"{tech_compliance.get('score', 0):.0f}%",
            delta=f"{tech_compliance.get('score', 0) - 85:.0f}%" if tech_compliance.get('score', 0) < 85 else None
        )
    
    with col2:
        st.metric(
            "Estimated Pages", 
            f"{tech_compliance.get('estimated_pages', 0):.1f}",
            delta=f"{tech_compliance.get('estimated_pages', 0) - 15:.1f}" if tech_compliance.get('estimated_pages', 0) > 15 else None
        )
    
    with col3:
        st.metric(
            "File Size (MB)", 
            f"{tech_compliance.get('file_size_mb', 0):.1f}",
            delta=f"{tech_compliance.get('file_size_mb', 0) - 10:.1f}" if tech_compliance.get('file_size_mb', 0) > 10 else None
        )
    
    with col4:
        issues_count = len(tech_compliance.get('issues', []))
        st.metric(
            "Compliance Issues", 
            issues_count,
            delta=f"+{issues_count}" if issues_count > 0 else None
        )
    
    # Issues list
    if tech_compliance.get('issues'):
        st.warning("Compliance Issues Detected:")
        for issue in tech_compliance['issues']:
            st.write(f"• {issue}")

def create_quality_assessment_dashboard(analysis_results: Dict):
    """Create quality assessment visualization"""
    
    st.subheader("Content Quality Assessment")
    
    quality_analysis = analysis_results.get("content_quality", {})
    
    if "error" in quality_analysis:
        st.error(quality_analysis["error"])
        return
    
    # Quality scores radar chart
    categories = []
    scores = []
    
    for key, value in quality_analysis.items():
        if isinstance(value, dict) and "score" in value:
            categories.append(key.replace("_", " ").title())
            scores.append(value["score"])
    
    if scores:
        fig_radar = go.Figure()
        
        fig_radar.add_trace(go.Scatterpolar(
            r=scores + [scores[0]],  # Close the polygon
            theta=categories + [categories[0]],
            fill='toself',
            name='Quality Scores',
            line_color='rgb(0, 100, 200)'
        ))
        
        fig_radar.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 5]
                )),
            showlegend=False,
            title="Content Quality Radar Chart"
        )
        
        st.plotly_chart(fig_radar, use_container_width=True)
        
        # Quality scores table
        quality_df = pd.DataFrame([
            {
                "Dimension": key.replace("_", " ").title(),
                "Score": f"{value['score']}/5",
                "Justification": value.get("justification", "N/A")
            }
            for key, value in quality_analysis.items()
            if isinstance(value, dict) and "score" in value
        ])
        
        st.dataframe(quality_df, use_container_width=True)

def create_section_coverage_dashboard(analysis_results: Dict):
    """Create section coverage visualization"""
    
    st.subheader("Section Coverage Analysis")
    
    section_analysis = analysis_results.get("section_coverage", {})
    
    if not section_analysis:
        st.warning("No section analysis available")
        return
    
    # Section coverage bar chart
    sections = []
    coverage_scores = []
    weights = []
    
    for section, data in section_analysis.items():
        sections.append(section.replace("_", " ").title())
        coverage_scores.append(data["coverage_score"])
        weights.append(data["weight"] * 100)
    
    fig_coverage = go.Figure()
    
    fig_coverage.add_trace(go.Bar(
        name='Coverage Score',
        x=sections,
        y=coverage_scores,
        yaxis='y',
        marker_color='lightblue'
    ))
    
    fig_coverage.add_trace(go.Scatter(
        name='Section Weight',
        x=sections,
        y=weights,
        yaxis='y2',
        mode='lines+markers',
        line=dict(color='red', width=2),
        marker=dict(size=8)
    ))
    
    fig_coverage.update_layout(
        title='Section Coverage vs Importance',
        xaxis_title='Sections',
        yaxis=dict(
            title='Coverage Score (%)',
            side='left'
        ),
        yaxis2=dict(
            title='Section Weight (%)',
            side='right',
            overlaying='y'
        ),
        legend=dict(x=0.7, y=1)
    )
    
    st.plotly_chart(fig_coverage, use_container_width=True)
    
    # Weighted coverage score
    total_weighted_score = sum(
        data["coverage_score"] * data["weight"] 
        for data in section_analysis.values()
    )
    
    st.metric("Overall Section Coverage", f"{total_weighted_score:.1f}%")

def create_recommendations_panel(analysis_results: Dict):
    """Create recommendations based on analysis"""
    
    st.subheader("Recommendations for Improvement")
    
    recommendations = []
    
    # Technical compliance recommendations
    tech_compliance = analysis_results.get("technical_compliance", {})
    if tech_compliance.get("score", 100) < 90:
        recommendations.append({
            "category": "Technical Compliance",
            "priority": "High",
            "recommendation": "Address technical compliance issues before submission",
            "details": tech_compliance.get("issues", [])
        })
    
    # Content quality recommendations
    quality_analysis = analysis_results.get("content_quality", {})
    low_scores = []
    for key, value in quality_analysis.items():
        if isinstance(value, dict) and value.get("score", 5) < 3:
            low_scores.append(key.replace("_", " ").title())
    
    if low_scores:
        recommendations.append({
            "category": "Content Quality",
            "priority": "High",
            "recommendation": f"Improve sections: {', '.join(low_scores)}",
            "details": ["Consider adding more detail and evidence", "Strengthen scientific rationale"]
        })
    
    # Section coverage recommendations
    section_analysis = analysis_results.get("section_coverage", {})
    weak_sections = [
        section.replace("_", " ").title()
        for section, data in section_analysis.items()
        if data["coverage_score"] < 60
    ]
    
    if weak_sections:
        recommendations.append({
            "category": "Section Coverage",
            "priority": "Medium",
            "recommendation": f"Strengthen coverage of: {', '.join(weak_sections)}",
            "details": ["Add more specific content", "Include relevant keywords and concepts"]
        })
    
    # Display recommendations
    for rec in recommendations:
        with st.expander(f"{rec['priority']} Priority: {rec['category']}"):
            st.write(f"**Recommendation:** {rec['recommendation']}")
            if rec.get("details"):
                st.write("**Details:**")
                for detail in rec["details"]:
                    st.write(f"• {detail}")

def main():
    st.title("COST 2025 Proposal Analyzer")
    st.markdown("Comprehensive analysis tool for COST Action proposals against 2025 requirements")
    
    # Initialize analyzer
    analyzer = COSTAnalyzer()
    
    # Sidebar navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox(
        "Choose Analysis Type",
        ["Document Upload & Analysis", "Deep Document Analysis", "Critical Review", "Technical Annex Analyzer", "Requirements Overview", "Policy Compliance", "Best Practices"]
    )
    
    if page == "Document Upload & Analysis":
        st.header("Technical Annex Analysis")
        
        # File upload
        uploaded_file = st.file_uploader(
            "Upload your Technical Annex",
            type=['pdf', 'docx'],
            help="Upload your COST Action Technical Annex in PDF or DOCX format"
        )
        
        if uploaded_file is not None:
            # Get file info
            file_size_mb = uploaded_file.size / (1024 * 1024)
            
            # Extract text
            with st.spinner("Processing document..."):
                if uploaded_file.type == "application/pdf":
                    text_content = analyzer.extract_text_from_pdf(uploaded_file)
                else:
                    text_content = analyzer.extract_text_from_docx(uploaded_file)
            
            if text_content:
                st.success(f"Document processed successfully! ({len(text_content)} characters)")
                
                # Run analysis
                with st.spinner("Analyzing document..."):
                    analysis_results = {
                        "technical_compliance": analyzer.analyze_technical_compliance(text_content, file_size_mb),
                        "content_quality": analyzer.analyze_content_quality(text_content),
                        "section_coverage": analyzer.analyze_section_coverage(text_content)
                    }
                
                # Create dashboard tabs
                tab1, tab2, tab3, tab4 = st.tabs(["Compliance", "Quality", "Coverage", "Recommendations"])
                
                with tab1:
                    create_compliance_dashboard(analyzer, analysis_results)
                
                with tab2:
                    create_quality_assessment_dashboard(analysis_results)
                
                with tab3:
                    create_section_coverage_dashboard(analysis_results)
                
                with tab4:
                    create_recommendations_panel(analysis_results)
                
                # Download analysis report
                if st.button("Generate Analysis Report"):
                    report_data = {
                        "timestamp": datetime.now().isoformat(),
                        "file_name": uploaded_file.name,
                        "analysis_results": analysis_results
                    }
                    
                    st.download_button(
                        label="Download Analysis Report (JSON)",
                        data=json.dumps(report_data, indent=2),
                        file_name=f"cost_analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                        mime="application/json"
                    )
            else:
                st.error("Could not extract text from the uploaded file")
    
    elif page == "Deep Document Analysis":
        create_deep_analysis_dashboard()
    
    elif page == "Critical Review":
        create_critical_review_dashboard()
    
    elif page == "Technical Annex Analyzer":
        create_technical_annex_comprehensive_analysis_tab()
    
    elif page == "Requirements Overview":
        st.header("COST 2025 Requirements Overview")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Technical Requirements")
            tech_req = analyzer.requirements["technical_format"]
            
            requirements_df = pd.DataFrame([
                {"Requirement": "Maximum Pages", "Value": tech_req["max_pages"]},
                {"Requirement": "Font", "Value": tech_req["font"]},
                {"Requirement": "Font Size", "Value": tech_req["font_size"]},
                {"Requirement": "Line Spacing", "Value": tech_req["line_spacing"]},
                {"Requirement": "Max File Size", "Value": f"{tech_req['max_file_size_mb']} MB"},
                {"Requirement": "Format", "Value": tech_req["format"]},
                {"Requirement": "Anonymity Required", "Value": "Yes" if tech_req["anonymity_required"] else "No"}
            ])
            
            st.dataframe(requirements_df, use_container_width=True)
        
        with col2:
            st.subheader("Network Requirements")
            net_req = analyzer.requirements["network_requirements"]
            
            st.write(f"**Minimum Countries:** {net_req['min_countries']}")
            st.write(f"**Minimum ITC Percentage:** {net_req['min_itc_percentage']}%")
            
            st.write("**ITC Countries:**")
            for country in net_req["itc_countries"]:
                st.write(f"• {country}")
        
        st.subheader("Evaluation Criteria")
        eval_criteria = analyzer.requirements["evaluation_criteria"]
        
        criteria_data = []
        for criterion, details in eval_criteria.items():
            criteria_data.append({
                "Criterion": criterion.title(),
                "Weight": f"{details['weight']*100:.0f}%",
                "Threshold": details['threshold'],
                "Subcriteria Count": len(details['subcriteria'])
            })
        
        st.dataframe(pd.DataFrame(criteria_data), use_container_width=True)
    
    elif page == "Policy Compliance":
        st.header("Policy Compliance Framework")
        
        st.subheader("Mission and Policies Visualization")
        
        # Sample data for policy compliance
        policy_data = {
            "ITC Participation": 58,
            "Female Leadership": 50,
            "Young Researchers": 45,
            "Industry Participation": 40
        }
        
        fig_policy = go.Figure(data=[
            go.Bar(
                x=list(policy_data.keys()),
                y=list(policy_data.values()),
                marker_color=['green' if v >= 50 else 'orange' if v >= 40 else 'red' for v in policy_data.values()]
            )
        ])
        
        fig_policy.update_layout(
            title="Policy Compliance Metrics (%)",
            yaxis_title="Percentage",
            showlegend=False
        )
        
        st.plotly_chart(fig_policy, use_container_width=True)
        
        # Policy requirements table
        st.subheader("Policy Requirements Details")
        
        policy_req = analyzer.policy_requirements
        
        for policy_type, requirements in policy_req.items():
            st.write(f"**{policy_type.replace('_', ' ').title()}:**")
            for req, value in requirements.items():
                st.write(f"• {req.replace('_', ' ').title()}: {value}")
    
    elif page == "Best Practices":
        st.header("COST Proposal Best Practices")
        
        st.subheader("Writing Guidelines")
        
        best_practices = {
            "State of the Art": [
                "Provide comprehensive literature review",
                "Identify clear research gaps",
                "Position your approach in context",
                "Include recent and relevant references"
            ],
            "Networking Rationale": [
                "Explain why networking is essential",
                "Demonstrate added value of collaboration",
                "Show complementary expertise",
                "Address geographic distribution benefits"
            ],
            "Impact and Objectives": [
                "Define clear, measurable objectives",
                "Link to societal challenges",
                "Demonstrate economic potential",
                "Include stakeholder engagement strategy"
            ],
            "Implementation": [
                "Provide realistic timeline",
                "Show adequate resource allocation",
                "Demonstrate project management capability",
                "Include risk mitigation strategies"
            ]
        }
        
        for section, practices in best_practices.items():
            with st.expander(f"{section} Best Practices"):
                for practice in practices:
                    st.write(f"• {practice}")
        
        st.subheader("Common Mistakes to Avoid")
        
        common_mistakes = [
            "Exceeding page limits",
            "Including identifying information (violating anonymity)",
            "Weak networking justification",
            "Unrealistic timelines or budgets",
            "Insufficient stakeholder engagement",
            "Poor geographic balance",
            "Lack of gender equality considerations",
            "Missing young researcher integration"
        ]
        
        for mistake in common_mistakes:
            st.write(f"❌ {mistake}")

if __name__ == "__main__":
    main()