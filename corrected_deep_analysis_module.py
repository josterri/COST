import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from typing import Dict, List, Tuple

class ActualCOSTDocumentAnalyzer:
    def __init__(self):
        # Actual content from the original COST Mission and Policies document
        self.actual_document_content = {
            "section_1_excellence_inclusiveness": {
                "title": "COST Excellence and Inclusiveness",
                "strategic_purpose": "Establishes dual foundation of excellence AND inclusiveness as core COST pillars",
                "sentences": [
                    {
                        "text": "The two pillars of COST excellence and inclusiveness are: Strengthening the excellence through the creation of cross-border networking of researchers; Promoting geographical, age and gender balance throughout its activities and operations",
                        "purpose": "Establishes fundamental COST philosophy - excellence AND inclusiveness as equal pillars",
                        "strategy": "Links excellence directly to networking, making collaboration a quality driver",
                        "positioning": "Positions their Action as embodying core COST values",
                        "critical_analysis": "Brilliant opening - doesn't treat inclusiveness as afterthought but as equal pillar with excellence"
                    },
                    {
                        "text": "In the Action proposal, 58% of the participating countries are ITCs",
                        "purpose": "Lead with strongest numerical evidence - 16% above minimum requirement",
                        "strategy": "Specific, verifiable statistic that dramatically exceeds expectations",
                        "positioning": "Demonstrates exceptional commitment to inclusiveness",
                        "critical_analysis": "58% is carefully calculated - high enough for credibility, not so high as to suggest geographical tokenism"
                    },
                    {
                        "text": "All COST activities are focused on cross-border collaboration, networking and dissemination of results",
                        "purpose": "Reinforces alignment with COST core mission using exact COST terminology",
                        "strategy": "Uses COST's own language to demonstrate ecosystem understanding",
                        "positioning": "Shows deep familiarity with COST priorities and values",
                        "critical_analysis": "Smart use of official language - evaluators will recognize their own terminology"
                    },
                    {
                        "text": "50% of key leadership positions in Action management are reserved for representatives from COST Inclusiveness Target Countries",
                        "purpose": "Demonstrates structural commitment to ITC empowerment in governance",
                        "strategy": "'Reserved' implies intentional planning, not reactive compliance",
                        "positioning": "Shows inclusiveness embedded in power structures",
                        "critical_analysis": "Exactly 50% - meets requirement precisely without over-commitment"
                    },
                    {
                        "text": "The Grant Holder will be from one of the ITCs",
                        "purpose": "Ultimate commitment signal - highest authority position to ITC representative",
                        "strategy": "Grant Holder = most powerful role, demonstrating serious commitment",
                        "positioning": "ITC leadership isn't symbolic but includes highest responsibility",
                        "critical_analysis": "Powerful statement - puts most authority and accountability with ITC representative"
                    }
                ]
            },
            "section_2_geographic_strategy": {
                "title": "Geographic and Resource Allocation Strategy",
                "sentences": [
                    {
                        "text": "Geographical, age and gender balance will be actively monitored and prioritized based on wide geographical inclusion and distribution across Europe",
                        "purpose": "Establishes systematic approach to diversity across multiple dimensions",
                        "strategy": "'Actively monitored' suggests ongoing commitment with accountability",
                        "positioning": "Professional, systematic approach to diversity management",
                        "critical_analysis": "Three-dimensional diversity (geography, age, gender) shows sophisticated understanding"
                    },
                    {
                        "text": "Networking tools will reserve at least 50% of the funds for Young Researchers and Innovators",
                        "purpose": "Financial commitment to next generation - not just participation but resources",
                        "strategy": "Concrete resource allocation demonstrates genuine investment",
                        "positioning": "Young researcher empowerment through substantial funding",
                        "critical_analysis": "50% of funds (not just positions) - significant financial commitment to youth development"
                    },
                    {
                        "text": "All ITCs will be members of the Action with at least 50% of funds allocated to them",
                        "purpose": "Double assurance - both membership AND financial allocation",
                        "strategy": "Addresses representation and resource distribution comprehensively",
                        "positioning": "Complete inclusiveness - participation plus resources",
                        "critical_analysis": "100% ITC membership + 50% funding = maximum possible inclusiveness commitment"
                    }
                ]
            },
            "section_3_stakeholder_collaboration": {
                "title": "Stakeholder Collaboration Strategy",
                "sentences": [
                    {
                        "text": "Enable fruitful collaborations between researchers, engineers, scholars and other stakeholders and business by providing a natural platform for them to meet and build mutual trust",
                        "purpose": "Establishes networking as relationship-building, not just meetings",
                        "strategy": "'Natural platform' and 'mutual trust' emphasize organic relationship development",
                        "positioning": "Understanding that effective networking requires trust and organic development",
                        "critical_analysis": "Lists specific stakeholder types - shows concrete target identification rather than vague promises"
                    },
                    {
                        "text": "In the inaugural Management Committee meeting, a Stakeholder Committee will be established",
                        "purpose": "Immediate implementation with specific timeline and structure",
                        "strategy": "First meeting commitment shows readiness and priority",
                        "positioning": "Stakeholder engagement as immediate priority, not eventual goal",
                        "critical_analysis": "Inaugural meeting = highest priority status for stakeholder engagement"
                    }
                ]
            },
            "section_4_industry_impact": {
                "title": "Industry Impact and Digital Finance Focus",
                "sentences": [
                    {
                        "text": "Substantial outreach to industry via the COST Action and substantial cooperations",
                        "purpose": "Claims existing industry relationships as credibility foundation",
                        "strategy": "'Substantial' (repeated) emphasizes scale and seriousness",
                        "positioning": "Experience-based credibility rather than future promises",
                        "critical_analysis": "Present tense suggests ongoing relationships, not hypothetical future plans"
                    },
                    {
                        "text": "Promote use and development of new technologies in Sustainable Digital Finance",
                        "purpose": "Specific research domain with contemporary relevance",
                        "strategy": "Sustainable Digital Finance hits multiple trending themes",
                        "positioning": "Cutting-edge research area with clear societal relevance",
                        "critical_analysis": "Triple trend alignment: sustainability + digitalization + finance = high impact potential"
                    },
                    {
                        "text": "All conferences and workshops will have at least 40% participation rate from industry",
                        "purpose": "Concrete measurable commitment to industry integration",
                        "strategy": "Specific percentage provides accountability and demonstrates ambition",
                        "positioning": "Quantified commitment shows serious industry engagement",
                        "critical_analysis": "40% is ambitious but achievable - shows realistic confidence in industry appeal"
                    }
                ]
            },
            "section_5_strategic_alignment": {
                "title": "COST Strategic Plan Alignment",
                "sentences": [
                    {
                        "text": "The Action has agreed to align all activities with the three COST strategic priorities",
                        "purpose": "Fundamental alignment statement with COST mission",
                        "strategy": "'Has agreed' suggests team consensus and commitment",
                        "positioning": "Mission-aligned partnership approach",
                        "critical_analysis": "'All activities' = comprehensive alignment, not selective compliance"
                    },
                    {
                        "text": "92% of ITCs are in the Action during the proposal phase",
                        "purpose": "Exceptional ITC engagement statistic",
                        "strategy": "92% is near-universal ITC participation",
                        "positioning": "Outstanding inclusiveness achievement",
                        "critical_analysis": "92% suggests either exceptional appeal or very strong existing networks"
                    },
                    {
                        "text": "45% of Action leadership positions allocated to young researchers and innovators",
                        "purpose": "Substantial youth empowerment commitment",
                        "strategy": "Significant leadership allocation to junior researchers",
                        "positioning": "Meaningful power-sharing with next generation",
                        "critical_analysis": "45% balances empowerment with experience - not tokenistic but substantial"
                    }
                ]
            },
            "section_6_gender_equality": {
                "title": "Gender Equality Implementation",
                "sentences": [
                    {
                        "text": "The Action is fully committed to the European Commission's Gender Equality Strategy 2020-2025 and the Gender Equality Plan for COST Activities",
                        "purpose": "Multi-level policy alignment (EU and COST)",
                        "strategy": "References both European and COST frameworks",
                        "positioning": "Comprehensive policy compliance",
                        "critical_analysis": "Specific strategy period (2020-2025) shows current policy knowledge"
                    },
                    {
                        "text": "All participating organisations will have a Gender Equality Plan within the first six months of the COST Action",
                        "purpose": "Institutional requirement with specific timeline",
                        "strategy": "Six-month deadline creates urgency and accountability",
                        "positioning": "Organization-wide policy requirement",
                        "critical_analysis": "Six months = serious timeline showing priority and implementation capability"
                    },
                    {
                        "text": "Action members will consider the GEAR Tool, sign up for the COST Gender Equality Community and the Gendered Innovations mailing list",
                        "purpose": "Multiple specific actions showing engagement ecosystem",
                        "strategy": "Lists concrete tools demonstrating insider knowledge",
                        "positioning": "Active participation in gender equality infrastructure",
                        "critical_analysis": "Very specific tools mentioned - suggests detailed knowledge of gender equality networks"
                    }
                ]
            }
        }

    def get_actual_strategic_insights(self) -> Dict:
        """Extract strategic insights from actual document content"""
        return {
            "overall_strategy": {
                "primary_approach": "Excellence Through Exceptional Inclusiveness",
                "positioning": "Sustainability-focused digital finance innovation with maximum inclusiveness",
                "credibility_building": "Specific metrics, existing achievements, concrete commitments",
                "risk_mitigation": "Multiple compliance dimensions, verifiable statistics, systematic implementation"
            },
            "numerical_brilliance": {
                "58_percent_itc": "16% above minimum - demonstrates serious commitment without tokenism",
                "92_percent_coverage": "Near-universal ITC engagement suggests exceptional appeal",
                "50_percent_pattern": "Consistent 50% across leadership, funding, participation",
                "45_percent_youth": "Substantial empowerment without compromising experience",
                "40_percent_industry": "Ambitious but realistic industry engagement target"
            },
            "language_mastery": {
                "cost_terminology": "Cross-border collaboration, networking, dissemination - exact COST language",
                "commitment_language": "Reserved, allocated, will be - strong commitment terms",
                "evidence_language": "Currently, already, substantial - present achievement focus",
                "strategic_language": "Actively monitored, systematically, comprehensive - professional approach"
            },
            "structural_genius": {
                "dual_pillar_opening": "Excellence AND inclusiveness as equal foundations",
                "front_loading": "Strongest metric (58%) in opening sentences",
                "escalating_commitment": "Participation → Leadership → Grant Holder (ultimate authority)",
                "resource_backing": "Not just positions but funding allocation (50% of funds)"
            }
        }

    def analyze_actual_sentence_effectiveness(self, sentence: Dict) -> Dict:
        """Analyze effectiveness of actual sentences from the document"""
        effectiveness_score = 0
        factors = []
        
        # Numerical evidence bonus
        if any(char.isdigit() for char in sentence["text"]):
            effectiveness_score += 25
            factors.append("Contains specific numerical evidence")
        
        # COST terminology bonus
        cost_terms = ["cross-border", "networking", "dissemination", "itc", "inclusiveness", "excellence"]
        if any(term.lower() in sentence["text"].lower() for term in cost_terms):
            effectiveness_score += 20
            factors.append("Uses official COST terminology")
        
        # Commitment strength bonus
        strong_terms = ["will", "allocated", "reserved", "committed", "established"]
        if any(term in sentence["text"].lower() for term in strong_terms):
            effectiveness_score += 15
            factors.append("Strong commitment language")
        
        # Present achievement bonus
        achievement_terms = ["currently", "already", "substantial", "existing"]
        if any(term in sentence["text"].lower() for term in achievement_terms):
            effectiveness_score += 15
            factors.append("Demonstrates existing achievements")
        
        # Specificity bonus
        specific_terms = ["50%", "58%", "92%", "45%", "40%", "six months"]
        if any(term in sentence["text"] for term in specific_terms):
            effectiveness_score += 20
            factors.append("Highly specific commitments")
        
        # Length assessment
        word_count = len(sentence["text"].split())
        if word_count > 35:
            effectiveness_score -= 10
            factors.append("Sentence complexity may reduce impact")
        
        return {
            "score": min(100, effectiveness_score),
            "factors": factors,
            "word_count": word_count,
            "character_count": len(sentence["text"])
        }

def create_actual_document_analysis_dashboard():
    """Create analysis dashboard for the actual COST document"""
    
    st.title("📋 Actual COST Mission & Policies Deep Analysis")
    st.markdown("**Analysis of the real 'COST Mission and Policies Original' document content**")
    
    analyzer = ActualCOSTDocumentAnalyzer()
    strategic_insights = analyzer.get_actual_strategic_insights()
    
    # Document Overview
    st.header("📊 Document Overview")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Research Focus", "Sustainable Digital Finance")
    
    with col2:
        st.metric("ITC Participation", "58%", delta="+8% above minimum")
    
    with col3:
        st.metric("ITC Coverage", "92%", delta="Near universal")
    
    with col4:
        st.metric("Industry Target", "40%", delta="Conferences/workshops")
    
    # Strategic Insights Overview
    st.header("🎯 Strategic Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Overall Strategy")
        for key, value in strategic_insights['overall_strategy'].items():
            st.write(f"**{key.replace('_', ' ').title()}:** {value}")
    
    with col2:
        st.subheader("Numerical Brilliance")
        for metric, analysis in strategic_insights['numerical_brilliance'].items():
            st.write(f"**{metric.replace('_', ' ').title()}:** {analysis}")
    
    # Language and Structure Analysis
    st.header("📝 Language and Structure Mastery")
    
    tab1, tab2, tab3 = st.tabs(["Language Mastery", "Structural Genius", "Document Flow"])
    
    with tab1:
        language_mastery = strategic_insights['language_mastery']
        for category, details in language_mastery.items():
            st.write(f"**{category.replace('_', ' ').title()}:** {details}")
    
    with tab2:
        structural_genius = strategic_insights['structural_genius']
        for element, description in structural_genius.items():
            st.write(f"**{element.replace('_', ' ').title()}:** {description}")
    
    with tab3:
        st.write("**Document Flow Analysis:**")
        flow_elements = [
            "Opens with COST philosophy alignment (excellence + inclusiveness)",
            "Immediately provides strongest evidence (58% ITC)",
            "Escalates commitment level (participation → leadership → Grant Holder)",
            "Backs commitments with resources (50% funding allocation)",
            "Provides concrete implementation (six-month timelines)",
            "Closes with systematic monitoring and accountability"
        ]
        for i, element in enumerate(flow_elements, 1):
            st.write(f"{i}. {element}")
    
    # Detailed Section Analysis
    st.header("🔍 Section-by-Section Analysis")
    
    sections = [
        ("section_1_excellence_inclusiveness", "🎯 Excellence & Inclusiveness"),
        ("section_2_geographic_strategy", "🌍 Geographic Strategy"),
        ("section_3_stakeholder_collaboration", "🤝 Stakeholder Collaboration"),
        ("section_4_industry_impact", "🏭 Industry Impact"),
        ("section_5_strategic_alignment", "📋 Strategic Alignment"),
        ("section_6_gender_equality", "⚖️ Gender Equality")
    ]
    
    for section_key, section_title in sections:
        section = analyzer.actual_document_content[section_key]
        
        st.subheader(f"{section_title}: {section['title']}")
        st.markdown(f"**Strategic Purpose:** {section.get('strategic_purpose', 'N/A')}")
        
        if 'sentences' in section:
            for i, sentence in enumerate(section['sentences'], 1):
                st.markdown(f"**Sentence {i}:** {sentence['text']}")
                
                # Analysis in columns
                col1, col2 = st.columns(2)
                
                with col1:
                    st.write(f"**Purpose:** {sentence['purpose']}")
                    st.write(f"**Strategy:** {sentence['strategy']}")
                
                with col2:
                    st.write(f"**Positioning:** {sentence['positioning']}")
                    st.write(f"**Critical Analysis:** {sentence['critical_analysis']}")
                
                # Effectiveness metrics
                effectiveness = analyzer.analyze_actual_sentence_effectiveness(sentence)
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Effectiveness", f"{effectiveness['score']}/100")
                with col2:
                    st.metric("Words", effectiveness['word_count'])
                with col3:
                    st.metric("Characters", effectiveness['character_count'])
                
                if effectiveness['factors']:
                    st.write("**Effectiveness Factors:**")
                    for factor in effectiveness['factors']:
                        st.write(f"• {factor}")
                
                st.write("---")
    
    # Sentence Effectiveness Visualization
    st.header("📈 Sentence Effectiveness Analysis")
    
    # Collect all sentences for visualization
    all_sentences = []
    for section_key, section in analyzer.actual_document_content.items():
        if 'sentences' in section:
            for i, sentence in enumerate(section['sentences']):
                effectiveness = analyzer.analyze_actual_sentence_effectiveness(sentence)
                all_sentences.append({
                    "Section": section['title'],
                    "Sentence": sentence['text'][:50] + "...",
                    "Effectiveness": effectiveness['score'],
                    "Word_Count": effectiveness['word_count'],
                    "Purpose": sentence['purpose']
                })
    
    if all_sentences:
        df = pd.DataFrame(all_sentences)
        
        fig = px.scatter(
            df,
            x="Word_Count",
            y="Effectiveness",
            color="Section",
            size=[10] * len(df),
            hover_data=["Sentence", "Purpose"],
            title="Sentence Effectiveness vs Length"
        )
        
        fig.update_layout(height=500)
        st.plotly_chart(fig, use_container_width=True)
    
    # Key Insights Summary
    st.header("💡 Key Strategic Insights")
    
    insights = [
        {
            "category": "🎯 Strategic Brilliance",
            "items": [
                "58% ITC participation (16% above minimum) - calculated excellence without tokenism",
                "Grant Holder from ITC - ultimate authority commitment signal",
                "50% funding allocation (not just participation) - resource-backed inclusiveness",
                "Sustainable Digital Finance focus - triple trend alignment (sustainability + digital + finance)",
                "92% ITC coverage - near-universal engagement demonstrates exceptional appeal"
            ]
        },
        {
            "category": "📝 Language Mastery",
            "items": [
                "Uses exact COST terminology (cross-border collaboration, networking, dissemination)",
                "Present tense achievements ('currently', 'already', 'substantial')",
                "Strong commitment language ('reserved', 'allocated', 'will be')",
                "Specific timeframes ('six months', 'inaugural meeting')",
                "Professional monitoring language ('actively monitored', 'systematically')"
            ]
        },
        {
            "category": "🏗️ Structural Genius",
            "items": [
                "Opens with COST philosophy (excellence + inclusiveness as equal pillars)",
                "Front-loads strongest evidence (58% ITC) for immediate impact",
                "Escalating commitment (participation → leadership → Grant Holder)",
                "Resource backing (not just promises but funding allocation)",
                "Concrete implementation (specific timelines and accountability)"
            ]
        },
        {
            "category": "⚠️ Potential Vulnerabilities",
            "items": [
                "Heavy reliance on numerical evidence - may cause 'metric fatigue'",
                "Limited innovation language - more compliance-focused than breakthrough-oriented",
                "Some complex sentences could be simplified for better impact",
                "Missing explicit connection to current EU priorities (recovery, resilience)",
                "Sustainable Digital Finance could be developed more strategically"
            ]
        }
    ]
    
    for insight_category in insights:
        st.subheader(f"{insight_category['category']} Analysis")
        for item in insight_category['items']:
            st.write(f"• {item}")
        st.write("")
    
    # Success Factors
    st.header("🚀 Why This Document Works")
    
    success_factors = [
        "**Front-Loading Excellence**: Leads with strongest evidence (58% ITC) for immediate credibility",
        "**Escalating Commitment**: Moves from participation to leadership to ultimate authority (Grant Holder)",
        "**Resource Backing**: Not just promises but concrete funding allocation (50% of funds)",
        "**COST Language Fluency**: Uses exact terminology evaluators recognize and value",
        "**Multi-Dimensional Strategy**: Addresses geography, gender, age, and industry simultaneously",
        "**Present Achievement Focus**: Emphasizes current capabilities rather than future promises",
        "**Systematic Implementation**: Provides concrete timelines and accountability mechanisms"
    ]
    
    for factor in success_factors:
        st.write(factor)

if __name__ == "__main__":
    create_actual_document_analysis_dashboard()