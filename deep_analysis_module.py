import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from typing import Dict, List, Tuple

class COSTDocumentDeepAnalyzer:
    def __init__(self):
        # Original document structure with deep analysis
        self.original_document_analysis = {
            "section_1": {
                "title": "EXCELLENCE AND INCLUSIVENESS POLICY",
                "strategic_purpose": "Establishes immediate compliance credibility and demonstrates exceed-not-meet mentality",
                "sentences": [
                    {
                        "text": "Those will be addressed as follows:",
                        "purpose": "Bridge sentence creating logical flow from implicit COST strategic priorities",
                        "strategy": "Assumes evaluator knowledge while creating expectation of systematic approach",
                        "positioning": "Professional, confident tone suggesting thorough preparation"
                    },
                    {
                        "text": "In our Action proposal, 58% of the participating countries are ITCs.",
                        "purpose": "Lead with strongest compliance metric - exceeds 50% requirement by significant margin",
                        "strategy": "Immediate credibility establishment through specific, verifiable number",
                        "positioning": "Demonstrates strategic geographic planning, not accidental compliance",
                        "critical_analysis": "58% is carefully chosen - high enough to show commitment, not so high as to suggest tokenism"
                    },
                    {
                        "text": "All of our COST activities are focused on cross-border collaboration, networking and dissemination of results.",
                        "purpose": "Reinforces core COST mission alignment before diving into specifics",
                        "strategy": "Uses COST's own language ('cross-border collaboration, networking, dissemination')",
                        "positioning": "Shows understanding of fundamental COST values beyond just compliance"
                    },
                    {
                        "text": "58% of the participating countries are ITC.",
                        "purpose": "Strategic repetition for emphasis and memorability",
                        "strategy": "Repetition is intentional - key metric worth reinforcing",
                        "positioning": "Confidence in this achievement warrants double mention",
                        "critical_analysis": "Redundancy suggests this is their strongest selling point"
                    },
                    {
                        "text": "We have reserved 50% of the key leadership positions in the Action management to a representative of a COST Inclusiveness Target Country.",
                        "purpose": "Demonstrates proactive planning rather than reactive compliance",
                        "strategy": "'Reserved' implies intentional allocation, not afterthought",
                        "positioning": "Shows structural commitment to inclusiveness in governance",
                        "critical_analysis": "Exactly 50% - meets requirement precisely, suggests calculated approach"
                    },
                    {
                        "text": "Those are:",
                        "purpose": "Creates anticipation and structured presentation of evidence",
                        "strategy": "Builds credibility through specific examples rather than vague promises",
                        "positioning": "Professional documentation style"
                    },
                    {
                        "text": "Two of the four working group leaders",
                        "purpose": "Specific operational detail proving implementation feasibility",
                        "strategy": "Concrete numbers (2 of 4) show actual planning depth",
                        "positioning": "Demonstrates thought-through organizational structure",
                        "critical_analysis": "50% exactly - mathematical precision suggests careful compliance calculation"
                    },
                    {
                        "text": "Vice-Chair of the Action or Grant Awarding Coordinator",
                        "purpose": "Shows senior-level ITC representation in key decision-making roles",
                        "strategy": "Names specific high-impact positions rather than generic roles",
                        "positioning": "Demonstrates meaningful power-sharing, not symbolic participation",
                        "critical_analysis": "'Or' suggests flexibility while ensuring senior ITC representation"
                    },
                    {
                        "text": "50% or more of the leadership positions will be allocated to female researchers.",
                        "purpose": "Addresses gender equality requirements with exceed-minimum commitment",
                        "strategy": "'Or more' suggests aspiration beyond minimum compliance",
                        "positioning": "Progressive stance on gender equality",
                        "critical_analysis": "Combines gender and leadership - double policy compliance in single statement"
                    }
                ]
            },
            "section_2": {
                "title": "Geographic and Demographic Strategy",
                "sentences": [
                    {
                        "text": "The Grant Holder will be from one of the ITCs.",
                        "purpose": "Demonstrates ultimate commitment - most powerful position goes to ITC",
                        "strategy": "Shows ITC leadership isn't symbolic but includes highest authority",
                        "positioning": "Credible commitment to inclusiveness at highest level",
                        "critical_analysis": "Grant Holder = most responsibility and visibility - strong signal"
                    },
                    {
                        "text": "Geographical, age and gender balance will be actively monitored and prioritized based on wide geographical inclusion and distribution across Europe.",
                        "purpose": "Establishes systematic approach to diversity beyond minimum requirements",
                        "strategy": "'Actively monitored' suggests ongoing commitment, not one-time compliance",
                        "positioning": "Proactive management approach to diversity",
                        "critical_analysis": "Mentions three diversity dimensions - comprehensive approach"
                    },
                    {
                        "text": "Our networking tools will reserve at least 50% of the funds for Young Researchers and Innovators.",
                        "purpose": "Financial commitment to young researcher development",
                        "strategy": "Concrete resource allocation demonstrates genuine commitment",
                        "positioning": "Investment in future, not just participation",
                        "critical_analysis": "50% of funds (not just positions) - substantial financial commitment"
                    }
                ]
            },
            "section_3": {
                "title": "Gender Equality and Young Researchers Strategy",
                "sentences": [
                    {
                        "text": "Gender balance is one of our goals and we will actively promote female participants in all our activities.",
                        "purpose": "Establishes gender equality as core objective, not compliance afterthought",
                        "strategy": "'All our activities' shows comprehensive integration",
                        "positioning": "Gender equality as fundamental value",
                        "critical_analysis": "Uses 'goal' language - aspirational rather than just compliant"
                    },
                    {
                        "text": "We currently have more than 50% female participants and actively maintain that ratio above 50% throughout the life-time of the Action.",
                        "purpose": "Proves track record while committing to sustained performance",
                        "strategy": "'Currently have' shows existing achievement, not future promise",
                        "positioning": "Evidence-based credibility with future commitment",
                        "critical_analysis": "Above 50% + 'throughout lifetime' = strong ongoing commitment"
                    },
                    {
                        "text": "All ITCs will be members of the Action and funds allocated will be at least 50%.",
                        "purpose": "Double assurance - participation AND financial allocation",
                        "strategy": "Addresses both representation and resource distribution",
                        "positioning": "Comprehensive inclusiveness beyond symbolic participation",
                        "critical_analysis": "100% ITC membership + 50% funding = maximum inclusiveness commitment"
                    },
                    {
                        "text": "We will also adhere and actively promote the latest GEP from the COST Action and the COST Scientific Committee.",
                        "purpose": "Demonstrates knowledge of current COST policies and commitment to evolution",
                        "strategy": "'Latest' shows they stay current with policy developments",
                        "positioning": "Engaged with COST governance, not just compliant",
                        "critical_analysis": "'Actively promote' goes beyond adherence to advocacy"
                    }
                ]
            },
            "section_4": {
                "title": "Participation of non-COST Countries and Specific Organisations",
                "strategic_purpose": "Brief section acknowledging global engagement without detail",
                "positioning": "Placeholder section - minimal content suggests this isn't their strength"
            },
            "section_5": {
                "title": "Collaborations between different stakeholders",
                "sentences": [
                    {
                        "text": "One of the main objectives of our Action is to enable fruitful collaborations between researchers, engineers, scholars and other stakeholders and business by providing a natural platform for them to meet and build mutual trust.",
                        "purpose": "Establishes networking as core mission using COST evaluation language",
                        "strategy": "'Natural platform' and 'mutual trust' suggest organic relationship building",
                        "positioning": "Understanding that networking is about relationship quality, not just meetings",
                        "critical_analysis": "Lists specific stakeholder types - shows concrete target identification"
                    },
                    {
                        "text": "In the inaugural MC meeting, we will set up a Stakeholder Committee with the first to write a stakeholder engagement strategy and plans to implement it.",
                        "purpose": "Demonstrates immediate implementation planning with concrete first steps",
                        "strategy": "Specific timeline ('inaugural MC meeting') shows readiness",
                        "positioning": "Systematic approach to stakeholder engagement",
                        "critical_analysis": "Committee formation + strategy + implementation = three-tier planning"
                    },
                    {
                        "text": "The Core Group will regularly report the progress of the engagement to the MC and take corrective actions if needed.",
                        "purpose": "Establishes accountability and feedback mechanisms",
                        "strategy": "Shows understanding that stakeholder engagement requires monitoring",
                        "positioning": "Professional project management approach",
                        "critical_analysis": "Reporting + corrective action = closed-loop management system"
                    }
                ]
            },
            "section_6": {
                "title": "Impact of research in the industrial sector",
                "sentences": [
                    {
                        "text": "We have substantial outreach to industry via our COST Action and substantial cooperations.",
                        "purpose": "Claims existing industry relationships as credibility foundation",
                        "strategy": "'Substantial' (repeated) emphasizes scale and depth",
                        "positioning": "Experience-based credibility",
                        "critical_analysis": "Present tense 'have' suggests ongoing relationships, not future plans"
                    },
                    {
                        "text": "One of our goals is to have a substantial impact of our research in the industrial sector.",
                        "purpose": "Explicit impact commitment targeting evaluation criteria",
                        "strategy": "Direct statement of impact objective",
                        "positioning": "Clear value proposition for industry",
                        "critical_analysis": "'Substantial impact' mirrors COST impact evaluation criterion"
                    },
                    {
                        "text": "We will achieve that by promoting the use and development of new technologies in the area of Sustainable Digital Finance.",
                        "purpose": "Specific technology domain focus with contemporary relevance",
                        "strategy": "'Sustainable Digital Finance' hits multiple trending themes",
                        "positioning": "Cutting-edge research area with clear industry relevance",
                        "critical_analysis": "Combines sustainability + digitalization + finance = triple trend alignment"
                    },
                    {
                        "text": "Throughout the research phase, we will actively work together with the Finance industry (this is already needed given the topic of our Action proposal).",
                        "purpose": "Establishes industry collaboration as necessity, not option",
                        "strategy": "Parenthetical reinforces logical connection",
                        "positioning": "Industry partnership as research requirement",
                        "critical_analysis": "Makes industry collaboration seem inevitable given research area"
                    },
                    {
                        "text": "Furthermore, our results and outcomes will be actively disseminated to SMEs as well as established players throughout Europe.",
                        "purpose": "Demonstrates broad dissemination strategy across company sizes",
                        "strategy": "SMEs + established players = comprehensive industry coverage",
                        "positioning": "Inclusive approach to industry engagement",
                        "critical_analysis": "European scope aligns with COST geographic mandate"
                    },
                    {
                        "text": "This will be done via the COST networking and dissemination tools, which will always require substantial involvement from the industry.",
                        "purpose": "Leverages COST infrastructure while ensuring industry engagement",
                        "strategy": "Uses COST's own tools showing system understanding",
                        "positioning": "Efficient use of existing COST mechanisms",
                        "critical_analysis": "'Always require' makes industry involvement non-negotiable"
                    },
                    {
                        "text": "We envision that all conferences and workshops will have at least a 40% participation rate from industry.",
                        "purpose": "Concrete measurable commitment to industry integration",
                        "strategy": "Specific percentage provides accountability metric",
                        "positioning": "Quantified commitment to industry engagement",
                        "critical_analysis": "40% is ambitious but achievable - shows realistic confidence"
                    }
                ]
            },
            "section_7": {
                "title": "COST Strategic Plan",
                "sentences": [
                    {
                        "text": "Our Action has agreed to align all activities with the three COST strategic priorities.",
                        "purpose": "Establishes fundamental alignment with COST mission",
                        "strategy": "'Has agreed' suggests team consensus and commitment",
                        "positioning": "Mission-aligned partnership with COST",
                        "critical_analysis": "'All activities' = comprehensive alignment, not selective compliance"
                    },
                    {
                        "text": "Indeed, all targets and Key Performance Indicators as defined in the COST Strategic Plan, March 2023, are already met during Proposal phase (as far as they concern that phase), have been agreed upon by the proposers (in so far COST MC decisions are concerned) or will be our guiding principles.",
                        "purpose": "Claims comprehensive KPI achievement with careful qualification",
                        "strategy": "Specific date reference (March 2023) shows current knowledge",
                        "positioning": "Detailed compliance awareness",
                        "critical_analysis": "Complex sentence with multiple qualifications suggests careful legal-style positioning"
                    },
                    {
                        "text": "Specifically:",
                        "purpose": "Transition to evidence presentation",
                        "strategy": "Creates expectation for detailed proof",
                        "positioning": "Systematic documentation approach"
                    }
                ]
            },
            "section_8": {
                "title": "Strategic Priority Evidence",
                "subsections": {
                    "5.1": {
                        "title": "Promoting and spreading excellence",
                        "evidence_points": [
                            {
                                "text": "92% of ITCs are in our Action during the proposal phase",
                                "purpose": "Exceptional ITC engagement well beyond requirements",
                                "strategy": "92% dramatically exceeds 50% minimum",
                                "positioning": "Outstanding inclusiveness achievement",
                                "critical_analysis": "Nearly universal ITC participation suggests exceptional appeal or existing networks"
                            },
                            {
                                "text": "At least five leadership positions are filled by ITC participants",
                                "purpose": "Concrete evidence of meaningful ITC leadership",
                                "strategy": "Specific number provides verifiable commitment",
                                "positioning": "Substantial ITC governance participation"
                            },
                            {
                                "text": "Our Action has agreed that 50% of the budget will be invested in ITCs/ activities and/or ITC researchers",
                                "purpose": "Financial commitment matching leadership commitment",
                                "strategy": "Budget allocation proves serious resource dedication",
                                "positioning": "Comprehensive inclusiveness across governance and resources"
                            },
                            {
                                "text": "50% of leadership positions will be occupied by female researchers",
                                "purpose": "Gender parity in leadership roles",
                                "strategy": "Exact parity shows balanced approach",
                                "positioning": "Gender equality in power structures"
                            }
                        ]
                    },
                    "5.2": {
                        "title": "Fostering interdisciplinary research for breakthrough science",
                        "purpose": "Addresses second strategic priority",
                        "critical_analysis": "Section title only - no content suggests this may be weaker area"
                    },
                    "5.3": {
                        "title": "Empowering and retaining young researchers and innovators",
                        "evidence_points": [
                            {
                                "text": "Our current share of young researchers and innovators is already above 50% (overall and for ITC) and we have agreed to maintain this ratio throughout the Action",
                                "purpose": "Demonstrates existing YRI strength with commitment to continuity",
                                "strategy": "Present achievement + future commitment",
                                "positioning": "YRI-rich environment with sustainability planning"
                            },
                            {
                                "text": "Our proposers have agreed to allocate 45% of Action leadership positions to young researchers and innovators",
                                "purpose": "Substantial YRI leadership commitment",
                                "strategy": "45% is significant leadership allocation to junior researchers",
                                "positioning": "Meaningful power-sharing with next generation"
                            },
                            {
                                "text": "As for the overall Action, we will also have a 50% share of female researchers among the young researchers, already above 50%",
                                "purpose": "Intersectional diversity - gender balance within YRI cohort",
                                "strategy": "Double diversity commitment (young + female)",
                                "positioning": "Sophisticated diversity understanding"
                            },
                            {
                                "text": "The share of women researchers and young researchers coming from ITC is already above 50% and we keep that throughout the Action",
                                "purpose": "Triple intersectionality - ITC + female + young",
                                "strategy": "Complex diversity matrix management",
                                "positioning": "Advanced inclusiveness sophistication"
                            }
                        ]
                    }
                }
            },
            "section_9": {
                "title": "COST Gender Equality Plan for COST Activities",
                "sentences": [
                    {
                        "text": "Our Action is fully committed to the European Commission's Gender Equality Strategy 2020-2025 and the Gender Equality Plan for COST Activities",
                        "purpose": "Alignment with EU-level and COST-specific gender policies",
                        "strategy": "References both EU and COST frameworks showing comprehensive awareness",
                        "positioning": "Multi-level policy compliance",
                        "critical_analysis": "Specific strategy period (2020-2025) shows current knowledge"
                    },
                    {
                        "text": "We will nominate a Gender Equality Advisor and have a substantial diversity team organizing Action events with a gender focus",
                        "purpose": "Dedicated resources and personnel for gender equality",
                        "strategy": "Advisor + team = institutional commitment",
                        "positioning": "Systematic approach to gender equality implementation"
                    },
                    {
                        "text": "Gender equality will also be monitored on the level of research projects",
                        "purpose": "Extends gender consideration to actual research work",
                        "strategy": "Project-level monitoring ensures comprehensive coverage",
                        "positioning": "Integration into core activities, not just administration"
                    },
                    {
                        "text": "All participating organisations will have a Gender Equality Plan within the first six months of the COST Action",
                        "purpose": "Institutional requirement with specific timeline",
                        "strategy": "Six-month deadline creates urgency and accountability",
                        "positioning": "Organization-wide policy requirement"
                    },
                    {
                        "text": "Our Action members will consider the GEAR Tool, sign up for the COST Gender Equality Community and the Gendered Innovations' mailing list for the latest gender-related news as well as cite and link in their publications to EU gender equality initiatives",
                        "purpose": "Multiple specific actions demonstrating engagement ecosystem",
                        "strategy": "Lists concrete actions showing detailed knowledge of gender equality infrastructure",
                        "positioning": "Active participation in gender equality community",
                        "critical_analysis": "Very specific tools mentioned suggests insider knowledge of gender equality networks"
                    }
                ]
            }
        }

    def get_strategic_insights(self) -> Dict:
        """Extract strategic insights from the document structure"""
        return {
            "overall_strategy": {
                "primary_approach": "Excellence through Exceeding Requirements",
                "positioning": "Sophisticated compliance with deep COST ecosystem understanding",
                "credibility_building": "Specific numbers, existing achievements, systematic planning",
                "risk_mitigation": "Multiple compliance dimensions, detailed evidence, systematic monitoring"
            },
            "numerical_strategy": {
                "58%_itc_participation": "Dramatically exceeds 50% minimum - shows serious inclusiveness commitment",
                "92%_itc_coverage": "Near-universal ITC engagement suggests exceptional networking or existing relationships",
                "50%_repeated_metrics": "Gender parity, ITC leadership, budget allocation - consistent 50% messaging",
                "45%_yri_leadership": "Substantial youth empowerment without compromising senior guidance",
                "40%_industry_participation": "Ambitious but realistic industry engagement target"
            },
            "language_patterns": {
                "confidence_indicators": ["substantial", "actively", "already", "throughout", "comprehensive"],
                "compliance_terms": ["adhere", "align", "commit", "reserve", "allocate", "maintain"],
                "evidence_language": ["specific", "concrete", "measurable", "verifiable", "systematic"],
                "future_commitment": ["will", "maintain", "continue", "monitor", "implement"]
            },
            "structural_analysis": {
                "front_loading": "Strongest evidence (58% ITC) appears first for maximum impact",
                "repetition_strategy": "Key metrics repeated for emphasis and memorability",
                "detail_gradation": "More detail in stronger areas, less in weaker areas",
                "evidence_hierarchy": "Numbers > specific commitments > general statements"
            }
        }

    def analyze_sentence_effectiveness(self, sentence: Dict) -> Dict:
        """Analyze individual sentence effectiveness"""
        effectiveness_score = 0
        factors = []
        
        # Specificity bonus
        if any(char.isdigit() for char in sentence["text"]):
            effectiveness_score += 20
            factors.append("Contains specific numbers")
        
        # Action language bonus
        action_words = ["will", "allocate", "reserve", "maintain", "monitor", "implement"]
        if any(word in sentence["text"].lower() for word in action_words):
            effectiveness_score += 15
            factors.append("Uses commitment language")
        
        # Evidence language bonus
        evidence_words = ["specific", "concrete", "already", "currently", "substantial"]
        if any(word in sentence["text"].lower() for word in evidence_words):
            effectiveness_score += 15
            factors.append("Provides evidence")
        
        # COST terminology bonus
        cost_terms = ["ITC", "inclusiveness", "networking", "collaboration", "dissemination"]
        if any(term.lower() in sentence["text"].lower() for term in cost_terms):
            effectiveness_score += 10
            factors.append("Uses COST terminology")
        
        # Length penalty for overly complex sentences
        if len(sentence["text"].split()) > 30:
            effectiveness_score -= 10
            factors.append("Overly complex sentence")
        
        return {
            "score": min(100, effectiveness_score),
            "factors": factors,
            "word_count": len(sentence["text"].split()),
            "character_count": len(sentence["text"])
        }

    def assess_sentence_strategy(self, sentence: Dict) -> Dict:
        """Assess strategic value of individual sentence"""
        assessment = {
            "credibility_building": 0,
            "compliance_demonstration": 0,
            "specificity_level": 0,
            "future_commitment": 0,
            "evidence_strength": 0
        }
        
        text = sentence["text"].lower()
        
        # Credibility building
        credibility_terms = ["already", "currently", "have", "existing", "proven", "established"]
        assessment["credibility_building"] = min(5, sum(2 for term in credibility_terms if term in text))
        
        # Compliance demonstration
        compliance_terms = ["50%", "58%", "92%", "itc", "gender", "young researchers", "allocate"]
        assessment["compliance_demonstration"] = min(5, sum(1 for term in compliance_terms if term in text))
        
        # Specificity level
        if any(char.isdigit() for char in sentence["text"]):
            assessment["specificity_level"] += 3
        if "specific" in text or "concrete" in text:
            assessment["specificity_level"] += 2
        assessment["specificity_level"] = min(5, assessment["specificity_level"])
        
        # Future commitment
        future_terms = ["will", "maintain", "continue", "ensure", "monitor", "implement"]
        assessment["future_commitment"] = min(5, sum(1 for term in future_terms if term in text))
        
        # Evidence strength
        if "purpose" in sentence and ("demonstrates" in sentence["purpose"] or "proves" in sentence["purpose"]):
            assessment["evidence_strength"] += 3
        if any(char.isdigit() for char in sentence["text"]):
            assessment["evidence_strength"] += 2
        assessment["evidence_strength"] = min(5, assessment["evidence_strength"])
        
        return assessment

    def extract_critical_insights(self) -> Dict:
        """Extract critical insights from the document analysis"""
        return {
            "strategic_brilliance": [
                "58% ITC participation (16% above minimum) - calculated excellence strategy",
                "Strategic repetition of key metrics for emphasis and memorability",
                "Front-loading strongest evidence (58% ITC) for maximum evaluator impact",
                "Grant Holder from ITC - ultimate commitment signal at highest authority level",
                "Triple intersectionality management (ITC + female + young) shows sophisticated diversity understanding",
                "Uses COST's own language ('cross-border collaboration, networking, dissemination') for alignment",
                "Demonstrates existing achievements ('currently have', 'already') rather than empty promises"
            ],
            "strategic_weaknesses": [
                "Section 5.2 (Interdisciplinary research) completely empty - major gap in strategic priority",
                "Some overly complex sentences reduce clarity and impact",
                "Missing innovation and breakthrough science language for competitive edge",
                "Limited forward-looking vision statements beyond compliance",
                "Repetition of 58% ITC could suggest limited diversity of strong points"
            ],
            "deep_insights": {
                "numerical_psychology": [
                    "58% carefully chosen - high enough for credibility, not so high as to suggest tokenism",
                    "92% ITC coverage suggests exceptional existing networks or relationships",
                    "Exactly 50% repeated across metrics suggests calculated compliance approach",
                    "40% industry participation is ambitious but realistic - shows confidence without arrogance",
                    "45% young researcher leadership balances empowerment with experience"
                ],
                "language_strategy": [
                    "'Reserved' positions implies proactive planning rather than reactive compliance",
                    "'Substantial' used repeatedly to emphasize scale and seriousness",
                    "'Already' and 'currently' establish track record credibility",
                    "'Throughout the lifetime' shows long-term commitment beyond startup phase",
                    "Parenthetical clarifications show careful legal-style positioning"
                ],
                "positioning_tactics": [
                    "Opens with strongest metric (58%) for immediate credibility establishment",
                    "Places ultimate commitment (Grant Holder from ITC) in strategic middle position",
                    "Uses specific COST terminology to demonstrate ecosystem understanding",
                    "Combines compliance with aspiration ('50% or more') to show progressive stance",
                    "Addresses multiple policy dimensions simultaneously for comprehensive coverage"
                ],
                "evidence_hierarchy": [
                    "Specific numbers > general commitments > vague statements",
                    "Current achievements > future promises > aspirational goals",
                    "Concrete roles > general participation > symbolic involvement",
                    "Financial commitments > positional commitments > participation commitments",
                    "Measurable outcomes > process commitments > value statements"
                ]
            }
        }

def create_deep_analysis_dashboard():
    """Create the deep analysis dashboard for the Streamlit app"""
    
    st.title("Deep Document Analysis: Original COST Mission & Policies")
    st.markdown("Sentence-by-sentence strategic analysis of the original document")
    
    analyzer = COSTDocumentDeepAnalyzer()
    strategic_insights = analyzer.get_strategic_insights()
    
    # Overall Strategy Analysis
    st.header("🎯 Overall Strategic Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Primary Strategy")
        st.write(f"**Approach:** {strategic_insights['overall_strategy']['primary_approach']}")
        st.write(f"**Positioning:** {strategic_insights['overall_strategy']['positioning']}")
        st.write(f"**Credibility:** {strategic_insights['overall_strategy']['credibility_building']}")
        st.write(f"**Risk Mitigation:** {strategic_insights['overall_strategy']['risk_mitigation']}")
    
    with col2:
        st.subheader("Numerical Strategy Analysis")
        for metric, analysis in strategic_insights['numerical_strategy'].items():
            with st.expander(f"{metric.replace('_', ' ').title()}"):
                st.write(analysis)
    
    # Language Pattern Analysis
    st.header("📝 Language Pattern Analysis")
    
    patterns = strategic_insights['language_patterns']
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.write("**Confidence Indicators**")
        for term in patterns['confidence_indicators']:
            st.write(f"• {term}")
    
    with col2:
        st.write("**Compliance Terms**")
        for term in patterns['compliance_terms']:
            st.write(f"• {term}")
    
    with col3:
        st.write("**Evidence Language**")
        for term in patterns['evidence_language']:
            st.write(f"• {term}")
    
    with col4:
        st.write("**Future Commitments**")
        for term in patterns['future_commitment']:
            st.write(f"• {term}")
    
    # Sentence-by-Sentence Analysis
    st.header("🔍 Sentence-by-Sentence Analysis")
    
    # Create effectiveness visualization
    effectiveness_data = []
    section_data = []
    
    for section_key, section in analyzer.original_document_analysis.items():
        if "sentences" in section:
            for i, sentence in enumerate(section["sentences"]):
                effectiveness = analyzer.analyze_sentence_effectiveness(sentence)
                effectiveness_data.append({
                    "Section": section["title"],
                    "Sentence_Index": i + 1,
                    "Text": sentence["text"][:50] + "..." if len(sentence["text"]) > 50 else sentence["text"],
                    "Effectiveness_Score": effectiveness["score"],
                    "Word_Count": effectiveness["word_count"],
                    "Purpose": sentence["purpose"]
                })
        
        section_data.append({
            "Section": section["title"],
            "Strategic_Purpose": section.get("strategic_purpose", "Not specified"),
            "Sentence_Count": len(section.get("sentences", []))
        })
    
    # Effectiveness visualization
    if effectiveness_data:
        effectiveness_df = pd.DataFrame(effectiveness_data)
        
        fig_effectiveness = px.scatter(
            effectiveness_df, 
            x="Word_Count", 
            y="Effectiveness_Score",
            color="Section",
            size="Sentence_Index",
            hover_data=["Text", "Purpose"],
            title="Sentence Effectiveness Analysis"
        )
        
        fig_effectiveness.update_layout(
            xaxis_title="Word Count",
            yaxis_title="Effectiveness Score",
            height=500
        )
        
        st.plotly_chart(fig_effectiveness, use_container_width=True)
    
    # Detailed Section Analysis
    st.header("📊 Detailed Section Analysis")
    
    selected_section = st.selectbox(
        "Select Section for Detailed Analysis",
        options=list(analyzer.original_document_analysis.keys()),
        format_func=lambda x: analyzer.original_document_analysis[x]["title"]
    )
    
    if selected_section:
        section = analyzer.original_document_analysis[selected_section]
        
        st.subheader(f"Analysis: {section['title']}")
        
        if "strategic_purpose" in section:
            st.write(f"**Strategic Purpose:** {section['strategic_purpose']}")
        
        if "sentences" in section:
            for i, sentence in enumerate(section["sentences"]):
                with st.expander(f"Sentence {i+1}: {sentence['text'][:60]}..."):
                    st.write(f"**Full Text:** {sentence['text']}")
                    st.write(f"**Purpose:** {sentence['purpose']}")
                    st.write(f"**Strategy:** {sentence['strategy']}")
                    st.write(f"**Positioning:** {sentence['positioning']}")
                    
                    if "critical_analysis" in sentence:
                        st.markdown(f"**🔍 Critical Analysis:** {sentence['critical_analysis']}")
                    
                    # Add strategic assessment
                    st.markdown("**🎯 Strategic Assessment:**")
                    assessment = analyzer.assess_sentence_strategy(sentence)
                    for category, score in assessment.items():
                        st.write(f"• {category.replace('_', ' ').title()}: {score}/5")
                    
                    # Effectiveness metrics
                    effectiveness = analyzer.analyze_sentence_effectiveness(sentence)
                    
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("Effectiveness Score", f"{effectiveness['score']}/100")
                    with col2:
                        st.metric("Word Count", effectiveness['word_count'])
                    with col3:
                        st.metric("Character Count", effectiveness['character_count'])
                    
                    if effectiveness['factors']:
                        st.write("**Effectiveness Factors:**")
                        for factor in effectiveness['factors']:
                            st.write(f"• {factor}")
        
        # Section-specific insights
        if selected_section in ["section_8"]:  # Strategic Priority Evidence
            st.subheader("Evidence Quality Analysis")
            
            subsections = section.get("subsections", {})
            for subsection_key, subsection in subsections.items():
                st.write(f"**{subsection['title']}**")
                
                if "evidence_points" in subsection:
                    evidence_scores = []
                    for point in subsection["evidence_points"]:
                        effectiveness = analyzer.analyze_sentence_effectiveness(point)
                        evidence_scores.append(effectiveness["score"])
                    
                    avg_score = sum(evidence_scores) / len(evidence_scores) if evidence_scores else 0
                    st.metric(f"Average Evidence Quality", f"{avg_score:.1f}/100")
                
                elif "critical_analysis" in subsection:
                    st.warning(f"Critical Analysis: {subsection['critical_analysis']}")
    
    # Critical Analysis Summary
    st.header("🔍 Critical Analysis Summary")
    
    critical_insights = analyzer.extract_critical_insights()
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🎯 Strategic Brilliance")
        for insight in critical_insights["strategic_brilliance"]:
            st.success(f"✓ {insight}")
    
    with col2:
        st.subheader("⚠️ Strategic Weaknesses")
        for weakness in critical_insights["strategic_weaknesses"]:
            st.warning(f"• {weakness}")
    
    st.subheader("🧠 Deep Strategic Insights")
    for category, insights in critical_insights["deep_insights"].items():
        with st.expander(f"{category.replace('_', ' ').title()} Analysis"):
            for insight in insights:
                st.write(f"• {insight}")
    
    # Strategic Recommendations
    st.header("💡 Strategic Insights and Recommendations")
    
    insights = [
        {
            "category": "Strengths",
            "items": [
                "Exceptional ITC engagement (58% participation, 92% coverage)",
                "Specific, verifiable commitments with concrete numbers",
                "Systematic approach to monitoring and accountability",
                "Deep understanding of COST ecosystem and terminology",
                "Multi-dimensional diversity strategy (geographic, gender, age)"
            ]
        },
        {
            "category": "Strategic Positioning",
            "items": [
                "Front-loads strongest evidence for maximum impact",
                "Uses repetition strategically for key messages",
                "Demonstrates existing achievements rather than just promises",
                "Integrates compliance across multiple policy dimensions",
                "Shows sophisticated understanding of evaluation criteria"
            ]
        },
        {
            "category": "Areas for Enhancement",
            "items": [
                "Section 5.2 (Interdisciplinary research) lacks content detail",
                "Could strengthen innovation and breakthrough science language",
                "Some sentences are overly complex and could be simplified",
                "Missing specific metrics for some strategic priorities",
                "Could add more forward-looking vision statements"
            ]
        },
        {
            "category": "Lessons for 2025",
            "items": [
                "Maintain the exceed-minimum approach (58% vs 50% requirement)",
                "Keep specific numerical commitments for credibility",
                "Add new technical compliance language for 2025 requirements",
                "Strengthen sections that were previously underdeveloped",
                "Maintain the systematic monitoring and accountability language"
            ]
        }
    ]
    
    for insight_category in insights:
        with st.expander(f"{insight_category['category']} Analysis"):
            for item in insight_category['items']:
                st.write(f"• {item}")

if __name__ == "__main__":
    create_deep_analysis_dashboard()