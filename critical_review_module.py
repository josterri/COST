import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from typing import Dict, List, Tuple

class COSTCriticalReviewer:
    def __init__(self):
        # Comprehensive critical analysis of the original document
        self.critical_review = {
            "fundamental_strengths": {
                "title": "Fundamental Strengths",
                "analysis": [
                    {
                        "strength": "Numerical Excellence Strategy",
                        "evidence": "58% ITC participation, 92% ITC coverage, consistent 50% targets",
                        "why_effective": "Creates immediate credibility through quantifiable achievements that dramatically exceed minimum requirements",
                        "strategic_value": "High - establishes competitive advantage through superior compliance",
                        "sustainability": "High - based on existing networks and proven capabilities"
                    },
                    {
                        "strength": "Multi-Dimensional Compliance Integration",
                        "evidence": "Simultaneously addresses geographic (ITC), demographic (gender, age), and sectoral (industry) diversity",
                        "why_effective": "Demonstrates sophisticated understanding that COST evaluation considers multiple diversity dimensions",
                        "strategic_value": "Very High - comprehensive approach reduces risk of single-point failure",
                        "sustainability": "Medium - requires ongoing coordination across multiple axes"
                    },
                    {
                        "strength": "Evidence-Based Credibility Building",
                        "evidence": "Uses present tense ('currently have', 'already') rather than future promises",
                        "why_effective": "Reduces evaluator skepticism by demonstrating track record rather than aspirations",
                        "strategic_value": "High - differentiates from competitors making empty promises",
                        "sustainability": "High - builds on existing achievements"
                    }
                ]
            },
            "critical_weaknesses": {
                "title": "Critical Weaknesses and Blind Spots",
                "analysis": [
                    {
                        "weakness": "Section 5.2 Complete Vacuum",
                        "evidence": "Interdisciplinary research section contains only title, no content",
                        "impact": "Critical Gap - This is one of three core COST strategic priorities",
                        "risk_level": "SEVERE - Could trigger automatic rejection",
                        "why_problematic": "Signals either lack of understanding or weakness in breakthrough science capability",
                        "competitive_disadvantage": "Competitors with strong interdisciplinary narratives will score significantly higher"
                    },
                    {
                        "weakness": "Over-Reliance on Compliance Metrics",
                        "evidence": "Majority of content focuses on meeting requirements rather than vision or innovation",
                        "impact": "Missed Opportunity - Fails to inspire or demonstrate breakthrough potential",
                        "risk_level": "MODERATE - May score lower on excellence and impact criteria",
                        "why_problematic": "COST seeks transformative research, not just compliant networking",
                        "competitive_disadvantage": "Less inspiring than visionary proposals with bold scientific ambitions"
                    },
                    {
                        "weakness": "Innovation Language Deficit",
                        "evidence": "Minimal use of terms like 'breakthrough', 'cutting-edge', 'revolutionary', 'transformative'",
                        "impact": "Positioning Problem - Appears incremental rather than groundbreaking",
                        "risk_level": "MODERATE - Excellence criterion expects innovation emphasis",
                        "why_problematic": "COST explicitly seeks breakthrough science and technological advancement",
                        "competitive_disadvantage": "Innovation-focused proposals will appear more aligned with COST mission"
                    },
                    {
                        "weakness": "Sustainable Digital Finance Superficial Treatment",
                        "evidence": "Research area mentioned but not deeply explored or positioned strategically",
                        "impact": "Missed Strategic Opportunity - Fails to leverage highly relevant contemporary theme",
                        "risk_level": "MODERATE - Impact criterion values societal relevance",
                        "why_problematic": "This intersection (sustainability + digitalization + finance) is extremely timely but underexploited",
                        "competitive_disadvantage": "Proposals with deeper thematic development will show stronger impact potential"
                    }
                ]
            },
            "strategic_risks": {
                "title": "Strategic Risks and Vulnerabilities",
                "analysis": [
                    {
                        "risk": "Metric Fatigue Among Evaluators",
                        "description": "Heavy emphasis on percentages and numbers may cause evaluator numbness",
                        "probability": "Medium",
                        "impact": "Could reduce emotional engagement and memorability",
                        "mitigation_needed": "Balance quantitative evidence with qualitative vision and narrative"
                    },
                    {
                        "risk": "Compliance-First Perception",
                        "description": "Document reads as meeting requirements rather than pursuing excellence",
                        "probability": "High",
                        "impact": "May score lower on excellence and innovation criteria",
                        "mitigation_needed": "Lead with vision and scientific ambition, support with compliance evidence"
                    },
                    {
                        "risk": "Sectional Imbalance Exposure",
                        "description": "Strong sections (inclusiveness) highlight weak sections (interdisciplinary research)",
                        "probability": "High",
                        "impact": "Creates perception of uneven capability across strategic priorities",
                        "mitigation_needed": "Strengthen weak sections or redistribute content for better balance"
                    },
                    {
                        "risk": "Industry Partnership Credibility Gap",
                        "description": "Claims 'substantial cooperations' without specific evidence or partner names",
                        "probability": "Medium",
                        "impact": "Evaluators may question authenticity of industry engagement claims",
                        "mitigation_needed": "Provide specific examples, letters of support, or concrete partnership details"
                    }
                ]
            },
            "missed_opportunities": {
                "title": "Missed Strategic Opportunities",
                "analysis": [
                    {
                        "opportunity": "Sustainability Leadership Positioning",
                        "description": "Could position as THE European network for sustainable finance transformation",
                        "potential_impact": "Exceptional - sustainability is top EU priority",
                        "current_treatment": "Mentioned briefly without strategic development",
                        "enhancement_needed": "Develop sustainability leadership narrative with EU policy alignment"
                    },
                    {
                        "opportunity": "Digital Transformation Expertise",
                        "description": "Could emphasize cutting-edge digital finance innovation leadership",
                        "potential_impact": "High - digital transformation is critical contemporary challenge",
                        "current_treatment": "Limited to basic digital finance mention",
                        "enhancement_needed": "Showcase technological innovation capabilities and digital leadership"
                    },
                    {
                        "opportunity": "Post-COVID Economic Recovery Alignment",
                        "description": "Could connect sustainable digital finance to European economic recovery priorities",
                        "potential_impact": "Very High - directly addresses current EU strategic priorities",
                        "current_treatment": "Not addressed",
                        "enhancement_needed": "Explicit connection to recovery, resilience, and transformation themes"
                    },
                    {
                        "opportunity": "Breakthrough Science Narrative",
                        "description": "Could develop compelling story about paradigm-shifting research potential",
                        "potential_impact": "Critical - core COST evaluation criterion",
                        "current_treatment": "Essentially absent",
                        "enhancement_needed": "Fundamental addition of innovation and breakthrough science positioning"
                    }
                ]
            },
            "evaluator_psychology": {
                "title": "Evaluator Psychology and Perception Analysis",
                "insights": [
                    {
                        "psychological_factor": "Cognitive Load and Attention Management",
                        "current_approach": "Front-loads strongest evidence (58% ITC) for immediate positive impression",
                        "effectiveness": "Positive - creates strong first impression",
                        "concern": "May create expectation that isn't sustained throughout document",
                        "optimization": "Ensure consistent quality and engagement throughout entire document"
                    },
                    {
                        "psychological_factor": "Credibility vs Aspiration Balance",
                        "current_approach": "Heavy emphasis on existing achievements and track record",
                        "effectiveness": "Strong for credibility building",
                        "concern": "May appear risk-averse or lacking ambition",
                        "optimization": "Add visionary elements that show ambitious but achievable goals"
                    },
                    {
                        "psychological_factor": "Evaluator Expertise Alignment",
                        "current_approach": "Uses COST terminology and demonstrates policy knowledge",
                        "effectiveness": "Good for insider credibility",
                        "concern": "May not resonate with external or interdisciplinary evaluators",
                        "optimization": "Include broader scientific and societal impact language"
                    },
                    {
                        "psychological_factor": "Emotional Engagement and Memorability",
                        "current_approach": "Primarily rational/logical approach with metrics and compliance",
                        "effectiveness": "Good for systematic evaluation",
                        "concern": "Limited emotional engagement or inspirational content",
                        "optimization": "Add compelling vision, transformative potential, and societal benefit narratives"
                    }
                ]
            },
            "competitive_analysis": {
                "title": "Competitive Landscape Analysis",
                "assessment": [
                    {
                        "competitive_dimension": "Compliance Excellence",
                        "our_position": "Market Leading - 58% ITC, 92% coverage, systematic approach",
                        "competitive_risk": "Low - difficult for competitors to exceed these metrics",
                        "strategic_advantage": "Strong defensive position",
                        "recommendation": "Maintain and emphasize, but don't rely solely on this advantage"
                    },
                    {
                        "competitive_dimension": "Scientific Innovation",
                        "our_position": "Unclear/Weak - minimal innovation language, missing Section 5.2",
                        "competitive_risk": "Very High - innovation-focused proposals will outperform",
                        "strategic_advantage": "Potential severe disadvantage",
                        "recommendation": "Major investment needed in innovation narrative and breakthrough science positioning"
                    },
                    {
                        "competitive_dimension": "Societal Impact",
                        "our_position": "Moderate - sustainable digital finance has relevance but underdeveloped",
                        "competitive_risk": "Medium - depends on competitor focus areas",
                        "strategic_advantage": "Could be strengthened significantly",
                        "recommendation": "Develop comprehensive impact narrative connecting to EU priorities"
                    },
                    {
                        "competitive_dimension": "Implementation Feasibility",
                        "our_position": "Strong - detailed planning, existing networks, systematic approach",
                        "competitive_risk": "Low - implementation strengths are well-demonstrated",
                        "strategic_advantage": "Solid competitive position",
                        "recommendation": "Maintain emphasis while adding innovation elements"
                    }
                ]
            }
        }

    def get_overall_assessment(self) -> Dict:
        """Provide overall critical assessment"""
        return {
            "overall_grade": "B+ (Good with significant improvement potential)",
            "core_strengths": [
                "Exceptional compliance metrics and systematic approach",
                "Strong implementation feasibility and track record",
                "Sophisticated understanding of COST ecosystem",
                "Multi-dimensional diversity strategy"
            ],
            "critical_vulnerabilities": [
                "Missing interdisciplinary research content (Section 5.2)",
                "Insufficient innovation and breakthrough science emphasis",
                "Over-reliance on compliance rather than vision",
                "Underdeveloped research area positioning"
            ],
            "competitive_position": "Strong on implementation, weak on innovation",
            "success_probability": "65% - Strong foundation but needs innovation boost",
            "key_recommendations": [
                "URGENT: Develop Section 5.2 with compelling interdisciplinary narrative",
                "Add breakthrough science and innovation language throughout",
                "Strengthen sustainable digital finance strategic positioning",
                "Balance compliance evidence with visionary elements"
            ]
        }

    def analyze_sentence_problems(self) -> List[Dict]:
        """Analyze specific problematic sentences"""
        return [
            {
                "sentence": "Those will be addressed as follows:",
                "problem": "Weak transition that assumes evaluator knowledge",
                "severity": "Minor",
                "improvement": "Replace with: 'Our Action addresses COST's excellence and inclusiveness priorities through the following strategic commitments:'"
            },
            {
                "sentence": "58% of the participating countries are ITC.",
                "problem": "Redundant repetition within same paragraph",
                "severity": "Minor",
                "improvement": "Remove redundancy or rephrase as reinforcement with additional context"
            },
            {
                "sentence": "One of the main objectives of our Action is to enable fruitful collaborations...",
                "problem": "Vague language ('fruitful collaborations') lacks specificity and impact",
                "severity": "Moderate",
                "improvement": "Specify types of collaboration and expected breakthrough outcomes"
            },
            {
                "sentence": "We envision that all conferences and workshops will have at least a 40% participation rate from industry.",
                "problem": "'Envision' suggests aspiration rather than commitment; percentage seems arbitrary",
                "severity": "Moderate",
                "improvement": "Provide rationale for 40% target and strengthen commitment language"
            },
            {
                "sentence": "Our Action has agreed to align all activities with the three COST strategic priorities.",
                "problem": "Past tense 'has agreed' suggests completed action rather than ongoing commitment",
                "severity": "Minor",
                "improvement": "Use present/future tense: 'Our Action aligns all activities with...'"
            }
        ]

    def get_improvement_roadmap(self) -> Dict:
        """Provide structured improvement roadmap"""
        return {
            "immediate_fixes": [
                {
                    "issue": "Section 5.2 Complete Gap",
                    "action": "Develop 200-300 word interdisciplinary research narrative",
                    "timeline": "Priority 1 - Critical",
                    "effort": "High",
                    "impact": "Critical"
                },
                {
                    "issue": "Innovation Language Deficit",
                    "action": "Add breakthrough science terminology throughout document",
                    "timeline": "Priority 1 - Critical", 
                    "effort": "Medium",
                    "impact": "High"
                }
            ],
            "strategic_enhancements": [
                {
                    "area": "Sustainable Digital Finance Positioning",
                    "action": "Develop comprehensive narrative connecting to EU sustainability priorities",
                    "timeline": "Priority 2 - Important",
                    "effort": "High",
                    "impact": "High"
                },
                {
                    "area": "Vision and Ambition Balance",
                    "action": "Add transformative potential and breakthrough outcome statements",
                    "timeline": "Priority 2 - Important",
                    "effort": "Medium",
                    "impact": "Medium"
                }
            ],
            "polish_refinements": [
                {
                    "improvement": "Sentence Structure Optimization",
                    "action": "Simplify complex sentences and improve flow",
                    "timeline": "Priority 3 - Enhancement",
                    "effort": "Low",
                    "impact": "Low"
                },
                {
                    "improvement": "Industry Partnership Specificity",
                    "action": "Add concrete examples or commitments",
                    "timeline": "Priority 3 - Enhancement",
                    "effort": "Medium",
                    "impact": "Medium"
                }
            ]
        }

def create_critical_review_dashboard():
    """Create comprehensive critical review dashboard"""
    
    st.title("🔍 Critical Review: Original COST Mission & Policies")
    st.markdown("Comprehensive critical analysis identifying strengths, weaknesses, and improvement opportunities")
    
    reviewer = COSTCriticalReviewer()
    overall_assessment = reviewer.get_overall_assessment()
    
    # Overall Assessment Card
    st.header("📊 Overall Assessment")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Overall Grade", overall_assessment["overall_grade"])
    
    with col2:
        st.metric("Success Probability", overall_assessment["success_probability"])
    
    with col3:
        st.metric("Competitive Position", overall_assessment["competitive_position"])
    
    # Strengths vs Vulnerabilities
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("✅ Core Strengths")
        for strength in overall_assessment["core_strengths"]:
            st.success(f"• {strength}")
    
    with col2:
        st.subheader("⚠️ Critical Vulnerabilities")
        for vulnerability in overall_assessment["critical_vulnerabilities"]:
            st.error(f"• {vulnerability}")
    
    # Detailed Critical Analysis Sections
    st.header("🔬 Detailed Critical Analysis")
    
    analysis_sections = [
        ("fundamental_strengths", "💪 Fundamental Strengths"),
        ("critical_weaknesses", "🚨 Critical Weaknesses & Blind Spots"),
        ("strategic_risks", "⚡ Strategic Risks & Vulnerabilities"),
        ("missed_opportunities", "💎 Missed Strategic Opportunities"),
        ("evaluator_psychology", "🧠 Evaluator Psychology Analysis"),
        ("competitive_analysis", "🏆 Competitive Landscape Analysis")
    ]
    
    for section_key, section_title in analysis_sections:
        section_data = reviewer.critical_review[section_key]
        
        with st.expander(section_title):
            st.markdown(f"### {section_data['title']}")
            
            if section_key == "fundamental_strengths":
                for item in section_data["analysis"]:
                    st.markdown(f"**{item['strength']}**")
                    st.write(f"Evidence: {item['evidence']}")
                    st.write(f"Why Effective: {item['why_effective']}")
                    st.write(f"Strategic Value: {item['strategic_value']}")
                    st.write(f"Sustainability: {item['sustainability']}")
                    st.write("---")
            
            elif section_key == "critical_weaknesses":
                for item in section_data["analysis"]:
                    st.markdown(f"**🚨 {item['weakness']}**")
                    st.write(f"Evidence: {item['evidence']}")
                    st.error(f"Impact: {item['impact']}")
                    st.write(f"Risk Level: {item['risk_level']}")
                    st.write(f"Why Problematic: {item['why_problematic']}")
                    st.write(f"Competitive Disadvantage: {item['competitive_disadvantage']}")
                    st.write("---")
            
            elif section_key == "strategic_risks":
                for item in section_data["analysis"]:
                    st.markdown(f"**⚡ {item['risk']}**")
                    st.write(f"Description: {item['description']}")
                    st.write(f"Probability: {item['probability']}")
                    st.write(f"Impact: {item['impact']}")
                    st.write(f"Mitigation Needed: {item['mitigation_needed']}")
                    st.write("---")
            
            elif section_key == "missed_opportunities":
                for item in section_data["analysis"]:
                    st.markdown(f"**💎 {item['opportunity']}**")
                    st.write(f"Description: {item['description']}")
                    st.write(f"Potential Impact: {item['potential_impact']}")
                    st.write(f"Current Treatment: {item['current_treatment']}")
                    st.write(f"Enhancement Needed: {item['enhancement_needed']}")
                    st.write("---")
            
            elif section_key == "evaluator_psychology":
                for item in section_data["insights"]:
                    st.markdown(f"**🧠 {item['psychological_factor']}**")
                    st.write(f"Current Approach: {item['current_approach']}")
                    st.write(f"Effectiveness: {item['effectiveness']}")
                    st.write(f"Concern: {item['concern']}")
                    st.write(f"Optimization: {item['optimization']}")
                    st.write("---")
            
            elif section_key == "competitive_analysis":
                for item in section_data["assessment"]:
                    st.markdown(f"**🏆 {item['competitive_dimension']}**")
                    st.write(f"Our Position: {item['our_position']}")
                    st.write(f"Competitive Risk: {item['competitive_risk']}")
                    st.write(f"Strategic Advantage: {item['strategic_advantage']}")
                    st.write(f"Recommendation: {item['recommendation']}")
                    st.write("---")
    
    # Sentence-Level Problems
    st.header("📝 Sentence-Level Problems")
    
    sentence_problems = reviewer.analyze_sentence_problems()
    
    for problem in sentence_problems:
        with st.expander(f"Problem: {problem['sentence'][:50]}..."):
            st.write(f"**Sentence:** {problem['sentence']}")
            st.write(f"**Problem:** {problem['problem']}")
            st.write(f"**Severity:** {problem['severity']}")
            st.write(f"**Improvement:** {problem['improvement']}")
    
    # Improvement Roadmap
    st.header("🗺️ Improvement Roadmap")
    
    roadmap = reviewer.get_improvement_roadmap()
    
    # Create priority visualization
    priorities = []
    efforts = []
    impacts = []
    labels = []
    
    effort_map = {"Low": 1, "Medium": 2, "High": 3}
    impact_map = {"Low": 1, "Medium": 2, "High": 3, "Critical": 4}
    
    for category, items in roadmap.items():
        for item in items:
            if category == "immediate_fixes":
                priorities.append(1)
                labels.append(f"URGENT: {item['issue']}")
                efforts.append(effort_map[item['effort']])
                impacts.append(impact_map[item['impact']])
            elif category == "strategic_enhancements":
                priorities.append(2)
                labels.append(f"IMPORTANT: {item['area']}")
                efforts.append(effort_map[item['effort']])
                impacts.append(impact_map[item['impact']])
            else:
                priorities.append(3)
                labels.append(f"POLISH: {item['improvement']}")
                efforts.append(effort_map[item['effort']])
                impacts.append(impact_map[item['impact']])
    
    # Effort vs Impact visualization
    fig_roadmap = go.Figure()
    
    colors = ['red' if p == 1 else 'orange' if p == 2 else 'blue' for p in priorities]
    
    fig_roadmap.add_trace(go.Scatter(
        x=efforts,
        y=impacts,
        mode='markers+text',
        marker=dict(
            size=[15 if p == 1 else 12 if p == 2 else 8 for p in priorities],
            color=colors,
            opacity=0.7
        ),
        text=[label[:30] + "..." if len(label) > 30 else label for label in labels],
        textposition="top center",
        hovertext=labels,
        name="Improvements"
    ))
    
    fig_roadmap.update_layout(
        title="Improvement Roadmap: Effort vs Impact",
        xaxis_title="Implementation Effort",
        yaxis_title="Expected Impact",
        xaxis=dict(tickvals=[1, 2, 3], ticktext=["Low", "Medium", "High"]),
        yaxis=dict(tickvals=[1, 2, 3, 4], ticktext=["Low", "Medium", "High", "Critical"]),
        height=500
    )
    
    st.plotly_chart(fig_roadmap, use_container_width=True)
    
    # Detailed roadmap tables
    for category, category_name in [
        ("immediate_fixes", "🚨 Immediate Fixes (Priority 1)"),
        ("strategic_enhancements", "🎯 Strategic Enhancements (Priority 2)"),
        ("polish_refinements", "✨ Polish Refinements (Priority 3)")
    ]:
        with st.expander(category_name):
            items = roadmap[category]
            
            if category == "immediate_fixes":
                df = pd.DataFrame([
                    {
                        "Issue": item["issue"],
                        "Action Required": item["action"],
                        "Timeline": item["timeline"],
                        "Effort": item["effort"],
                        "Impact": item["impact"]
                    }
                    for item in items
                ])
            else:
                df = pd.DataFrame([
                    {
                        "Area" if category == "strategic_enhancements" else "Improvement": 
                        item.get("area", item.get("improvement")),
                        "Action Required": item["action"],
                        "Timeline": item["timeline"],
                        "Effort": item["effort"],
                        "Impact": item["impact"]
                    }
                    for item in items
                ])
            
            st.dataframe(df, use_container_width=True)
    
    # Key Recommendations Summary
    st.header("🎯 Key Recommendations Summary")
    
    for i, recommendation in enumerate(overall_assessment["key_recommendations"], 1):
        if "URGENT" in recommendation:
            st.error(f"{i}. {recommendation}")
        else:
            st.warning(f"{i}. {recommendation}")

if __name__ == "__main__":
    create_critical_review_dashboard()