import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from typing import Dict, List, Tuple, Any
import re
import json
from datetime import datetime

class TechnicalAnnexComprehensiveAnalyzer:
    def __init__(self):
        # Complete evaluation framework based on ALL COST 2025 requirements
        self.evaluation_framework = {
            "technical_format_requirements": {
                "mandatory_sections": [
                    "State-of-the-art",
                    "Rationale for choosing networking to address the main challenge", 
                    "Critical mass of the network",
                    "Impact related to objectives",
                    "Involvement of stakeholders",
                    "Communication, dissemination and valorisation",
                    "Action Structure",
                    "Work plan (tasks, activities and timeframe)",
                    "Deliverables",
                    "Gantt chart"
                ],
                "format_requirements": {
                    "max_pages": 15,
                    "font": "Arial",
                    "font_size": 10,
                    "line_spacing": 1,
                    "anonymity": "mandatory",
                    "template_modification": "forbidden",
                    "file_format": "PDF",
                    "max_file_size_mb": 10
                }
            },
            "evaluation_criteria_detailed": {
                "excellence_science_technology_networking": {
                    "weight": 33.3,
                    "threshold": 3.0,
                    "detailed_subcriteria": {
                        "scientific_innovation": {
                            "weight": 20,
                            "evaluation_points": [
                                "Breakthrough potential demonstrated",
                                "Novel approaches and methodologies",
                                "Scientific rigor and methodology quality",
                                "Originality of research questions",
                                "Advancement beyond current state-of-art"
                            ]
                        },
                        "technological_advancement": {
                            "weight": 20,
                            "evaluation_points": [
                                "Technology innovation potential",
                                "Technical feasibility demonstrated",
                                "Integration of cutting-edge technologies",
                                "Technological impact and applications",
                                "Technical risk assessment and mitigation"
                            ]
                        },
                        "networking_value_add": {
                            "weight": 30,
                            "evaluation_points": [
                                "Clear rationale for networking necessity",
                                "Demonstration of synergistic benefits",
                                "Complementary expertise integration",
                                "Collaboration mechanisms defined",
                                "Network sustainability and growth potential"
                            ]
                        },
                        "interdisciplinary_approach": {
                            "weight": 15,
                            "evaluation_points": [
                                "Multi-disciplinary integration demonstrated",
                                "Cross-sector collaboration evidence",
                                "Transdisciplinary methodology adoption",
                                "Integration of diverse perspectives",
                                "Holistic approach to complex challenges"
                            ]
                        },
                        "open_science_commitment": {
                            "weight": 15,
                            "evaluation_points": [
                                "Open access publication commitment",
                                "Data sharing and FAIR principles",
                                "Transparent methodology sharing",
                                "Reproducibility and replicability",
                                "Community engagement and participation"
                            ]
                        }
                    }
                },
                "impact": {
                    "weight": 33.3,
                    "threshold": 3.0,
                    "detailed_subcriteria": {
                        "societal_impact": {
                            "weight": 25,
                            "evaluation_points": [
                                "Clear societal challenges addressed",
                                "Citizen and community benefit demonstration",
                                "Social innovation potential",
                                "Public policy influence potential",
                                "Quality of life improvement pathways"
                            ]
                        },
                        "economic_impact": {
                            "weight": 25,
                            "evaluation_points": [
                                "Economic value creation potential",
                                "Industry transformation possibilities",
                                "Job creation and skill development",
                                "Market innovation and competitiveness",
                                "Economic sustainability assessment"
                            ]
                        },
                        "scientific_impact": {
                            "weight": 20,
                            "evaluation_points": [
                                "Contribution to knowledge advancement",
                                "Paradigm shift potential",
                                "Citation and influence potential",
                                "Scientific community benefit",
                                "Research methodology advancement"
                            ]
                        },
                        "stakeholder_engagement": {
                            "weight": 15,
                            "evaluation_points": [
                                "Meaningful stakeholder involvement",
                                "Industry partnership quality",
                                "End-user integration strategies",
                                "Policy maker engagement",
                                "Civil society participation"
                            ]
                        },
                        "un_sdg_alignment": {
                            "weight": 15,
                            "evaluation_points": [
                                "Clear UN SDG contribution",
                                "Sustainability goals advancement",
                                "Global challenge addressing",
                                "Environmental impact consideration",
                                "Social equity and inclusion"
                            ]
                        }
                    }
                },
                "implementation": {
                    "weight": 33.4,
                    "threshold": 3.0,
                    "detailed_subcriteria": {
                        "project_management": {
                            "weight": 25,
                            "evaluation_points": [
                                "Management structure clarity",
                                "Leadership capability demonstration",
                                "Governance framework adequacy",
                                "Decision-making processes",
                                "Quality assurance mechanisms"
                            ]
                        },
                        "timeline_milestone_realism": {
                            "weight": 20,
                            "evaluation_points": [
                                "Realistic timeline development",
                                "Milestone appropriateness",
                                "Critical path identification",
                                "Contingency planning",
                                "Progress monitoring systems"
                            ]
                        },
                        "resource_allocation": {
                            "weight": 20,
                            "evaluation_points": [
                                "Budget allocation efficiency",
                                "Resource optimization strategies",
                                "Co-funding arrangements",
                                "Infrastructure requirements",
                                "Human resource planning"
                            ]
                        },
                        "network_coordination": {
                            "weight": 20,
                            "evaluation_points": [
                                "Coordination mechanisms",
                                "Communication strategies",
                                "Conflict resolution processes",
                                "Cultural integration approaches",
                                "Virtual collaboration tools"
                            ]
                        },
                        "risk_management": {
                            "weight": 15,
                            "evaluation_points": [
                                "Risk identification comprehensiveness",
                                "Mitigation strategies quality",
                                "Contingency planning depth",
                                "Risk monitoring systems",
                                "Adaptive management approaches"
                            ]
                        }
                    }
                }
            },
            "cost_strategic_priorities_mapping": {
                "promoting_spreading_excellence": {
                    "required_elements": [
                        "ITC participation demonstration (minimum 50%)",
                        "Excellence in research and innovation",
                        "Knowledge transfer mechanisms",
                        "Capacity building strategies",
                        "Best practice sharing"
                    ]
                },
                "fostering_interdisciplinary_research": {
                    "required_elements": [
                        "Multi-disciplinary approach demonstration",
                        "Cross-sector collaboration",
                        "Breakthrough science potential",
                        "Innovation ecosystem integration",
                        "Transdisciplinary methodologies"
                    ]
                },
                "empowering_retaining_young_researchers": {
                    "required_elements": [
                        "Young researcher participation (target >50%)",
                        "Career development opportunities",
                        "Mentorship programs",
                        "Skill development initiatives",
                        "Leadership development pathways"
                    ]
                }
            },
            "policy_compliance_requirements": {
                "inclusiveness_policy": {
                    "itc_participation_minimum": 50,
                    "itc_leadership_allocation": 50,
                    "geographic_balance": True,
                    "capacity_building": True
                },
                "gender_equality": {
                    "female_participation_target": 50,
                    "gender_balance_monitoring": True,
                    "gender_equality_plan": True,
                    "gear_tool_integration": True
                },
                "research_integrity": {
                    "ethical_compliance": True,
                    "originality_requirement": True,
                    "intellectual_property_respect": True,
                    "peaceful_purposes": True
                }
            }
        }
        
        # Comprehensive sentence evaluation matrix
        self.sentence_evaluation_matrix = {
            "content_quality_metrics": {
                "specificity": {"weight": 20, "max_score": 5},
                "evidence_strength": {"weight": 25, "max_score": 5},
                "innovation_language": {"weight": 20, "max_score": 5},
                "networking_rationale": {"weight": 15, "max_score": 5},
                "impact_demonstration": {"weight": 20, "max_score": 5}
            },
            "compliance_metrics": {
                "policy_alignment": {"weight": 30, "max_score": 5},
                "requirement_coverage": {"weight": 25, "max_score": 5},
                "technical_compliance": {"weight": 25, "max_score": 5},
                "strategic_priority_mapping": {"weight": 20, "max_score": 5}
            }
        }

    def create_comprehensive_analysis_plan(self) -> Dict:
        """Create detailed analysis plan for technical annex evaluation"""
        return {
            "phase_1_document_parsing": {
                "tasks": [
                    "Extract and structure all text content",
                    "Identify section boundaries and headers",
                    "Parse sentences and paragraphs systematically",
                    "Create sentence-to-section mapping",
                    "Generate document structure analysis"
                ],
                "deliverables": [
                    "Structured text database",
                    "Section content mapping",
                    "Sentence inventory with metadata",
                    "Document structure visualization"
                ]
            },
            "phase_2_requirement_mapping": {
                "tasks": [
                    "Map each sentence to evaluation criteria",
                    "Identify requirement coverage gaps",
                    "Assess policy compliance per sentence",
                    "Evaluate strategic priority alignment",
                    "Create comprehensive coverage matrix"
                ],
                "deliverables": [
                    "Sentence-to-requirement mapping database",
                    "Coverage gap analysis report",
                    "Compliance assessment matrix",
                    "Strategic alignment evaluation"
                ]
            },
            "phase_3_content_quality_assessment": {
                "tasks": [
                    "Evaluate each sentence for content quality",
                    "Assess innovation and breakthrough language",
                    "Analyze evidence strength and specificity",
                    "Evaluate networking rationale quality",
                    "Assess impact demonstration effectiveness"
                ],
                "deliverables": [
                    "Sentence quality scores database",
                    "Content strength analysis report",
                    "Language effectiveness assessment",
                    "Evidence quality evaluation"
                ]
            },
            "phase_4_gap_analysis": {
                "tasks": [
                    "Identify missing content areas",
                    "Assess weak coverage sections",
                    "Evaluate competitive positioning",
                    "Analyze improvement opportunities",
                    "Generate prioritized recommendations"
                ],
                "deliverables": [
                    "Comprehensive gap analysis report",
                    "Improvement priority matrix",
                    "Competitive positioning assessment",
                    "Strategic enhancement recommendations"
                ]
            },
            "phase_5_optimization_recommendations": {
                "tasks": [
                    "Generate sentence-level improvements",
                    "Propose section enhancement strategies",
                    "Develop content strengthening plans",
                    "Create implementation roadmap",
                    "Provide success probability assessment"
                ],
                "deliverables": [
                    "Detailed improvement recommendations",
                    "Content optimization strategies",
                    "Implementation timeline",
                    "Success probability forecast"
                ]
            }
        }

    def analyze_sentence_against_all_criteria(self, sentence: str, section: str, position: int) -> Dict:
        """Comprehensive sentence analysis against all COST requirements"""
        analysis_result = {
            "sentence_metadata": {
                "text": sentence,
                "section": section,
                "position": position,
                "word_count": len(sentence.split()),
                "character_count": len(sentence)
            },
            "excellence_criteria_assessment": self._assess_excellence_criteria(sentence),
            "impact_criteria_assessment": self._assess_impact_criteria(sentence),
            "implementation_criteria_assessment": self._assess_implementation_criteria(sentence),
            "policy_compliance_assessment": self._assess_policy_compliance(sentence),
            "strategic_priority_alignment": self._assess_strategic_priorities(sentence),
            "content_quality_metrics": self._assess_content_quality(sentence),
            "improvement_recommendations": self._generate_sentence_improvements(sentence, section),
            "overall_score": 0  # Will be calculated
        }
        
        # Calculate overall score
        analysis_result["overall_score"] = self._calculate_overall_sentence_score(analysis_result)
        
        return analysis_result

    def _assess_excellence_criteria(self, sentence: str) -> Dict:
        """Assess sentence against excellence criteria"""
        assessment = {
            "scientific_innovation": 0,
            "technological_advancement": 0,
            "networking_value_add": 0,
            "interdisciplinary_approach": 0,
            "open_science_commitment": 0
        }
        
        text_lower = sentence.lower()
        
        # Scientific innovation indicators
        innovation_terms = ["breakthrough", "novel", "innovative", "cutting-edge", "revolutionary", "paradigm", "transformative"]
        assessment["scientific_innovation"] = min(5, sum(2 for term in innovation_terms if term in text_lower))
        
        # Technological advancement indicators
        tech_terms = ["technology", "digital", "advanced", "state-of-art", "sophisticated", "emerging"]
        assessment["technological_advancement"] = min(5, sum(1 for term in tech_terms if term in text_lower))
        
        # Networking value indicators
        network_terms = ["collaboration", "networking", "synergy", "complementary", "collective", "joint"]
        assessment["networking_value_add"] = min(5, sum(1 for term in network_terms if term in text_lower))
        
        # Interdisciplinary indicators
        interdisciplinary_terms = ["interdisciplinary", "multidisciplinary", "transdisciplinary", "cross-sector", "holistic"]
        assessment["interdisciplinary_approach"] = min(5, sum(2 for term in interdisciplinary_terms if term in text_lower))
        
        # Open science indicators
        open_science_terms = ["open access", "open data", "transparent", "reproducible", "fair principles"]
        assessment["open_science_commitment"] = min(5, sum(1 for term in open_science_terms if term in text_lower))
        
        return assessment

    def _assess_impact_criteria(self, sentence: str) -> Dict:
        """Assess sentence against impact criteria"""
        assessment = {
            "societal_impact": 0,
            "economic_impact": 0,
            "scientific_impact": 0,
            "stakeholder_engagement": 0,
            "un_sdg_alignment": 0
        }
        
        text_lower = sentence.lower()
        
        # Societal impact indicators
        societal_terms = ["society", "citizen", "community", "social", "public", "quality of life"]
        assessment["societal_impact"] = min(5, sum(1 for term in societal_terms if term in text_lower))
        
        # Economic impact indicators
        economic_terms = ["economic", "market", "industry", "commercial", "business", "economic value"]
        assessment["economic_impact"] = min(5, sum(1 for term in economic_terms if term in text_lower))
        
        # Scientific impact indicators
        scientific_terms = ["knowledge", "research", "scientific", "discovery", "understanding"]
        assessment["scientific_impact"] = min(5, sum(1 for term in scientific_terms if term in text_lower))
        
        # Stakeholder engagement indicators
        stakeholder_terms = ["stakeholder", "industry", "policy", "end-user", "partner"]
        assessment["stakeholder_engagement"] = min(5, sum(1 for term in stakeholder_terms if term in text_lower))
        
        # UN SDG alignment indicators
        sdg_terms = ["sustainable", "sustainability", "sdg", "environment", "climate", "equality"]
        assessment["un_sdg_alignment"] = min(5, sum(1 for term in sdg_terms if term in text_lower))
        
        return assessment

    def _assess_implementation_criteria(self, sentence: str) -> Dict:
        """Assess sentence against implementation criteria"""
        assessment = {
            "project_management": 0,
            "timeline_milestone_realism": 0,
            "resource_allocation": 0,
            "network_coordination": 0,
            "risk_management": 0
        }
        
        text_lower = sentence.lower()
        
        # Project management indicators
        pm_terms = ["management", "governance", "leadership", "coordination", "oversight"]
        assessment["project_management"] = min(5, sum(1 for term in pm_terms if term in text_lower))
        
        # Timeline indicators
        timeline_terms = ["timeline", "milestone", "schedule", "year", "month", "deadline"]
        assessment["timeline_milestone_realism"] = min(5, sum(1 for term in timeline_terms if term in text_lower))
        
        # Resource allocation indicators
        resource_terms = ["budget", "resource", "funding", "allocation", "investment"]
        assessment["resource_allocation"] = min(5, sum(1 for term in resource_terms if term in text_lower))
        
        # Network coordination indicators
        coordination_terms = ["coordination", "communication", "collaboration", "integration"]
        assessment["network_coordination"] = min(5, sum(1 for term in coordination_terms if term in text_lower))
        
        # Risk management indicators
        risk_terms = ["risk", "mitigation", "contingency", "challenge", "uncertainty"]
        assessment["risk_management"] = min(5, sum(1 for term in risk_terms if term in text_lower))
        
        return assessment

    def _assess_policy_compliance(self, sentence: str) -> Dict:
        """Assess sentence against policy compliance requirements"""
        assessment = {
            "inclusiveness_demonstration": 0,
            "gender_equality_commitment": 0,
            "young_researcher_integration": 0,
            "research_integrity": 0
        }
        
        text_lower = sentence.lower()
        
        # Inclusiveness indicators
        inclusiveness_terms = ["itc", "inclusiveness", "geographic", "diversity", "participation"]
        assessment["inclusiveness_demonstration"] = min(5, sum(1 for term in inclusiveness_terms if term in text_lower))
        
        # Gender equality indicators
        gender_terms = ["gender", "female", "women", "equality", "balance"]
        assessment["gender_equality_commitment"] = min(5, sum(1 for term in gender_terms if term in text_lower))
        
        # Young researcher indicators
        young_terms = ["young", "early career", "phd", "postdoc", "researcher"]
        assessment["young_researcher_integration"] = min(5, sum(1 for term in young_terms if term in text_lower))
        
        # Research integrity indicators
        integrity_terms = ["ethical", "integrity", "responsible", "original", "honest"]
        assessment["research_integrity"] = min(5, sum(1 for term in integrity_terms if term in text_lower))
        
        return assessment

    def _assess_strategic_priorities(self, sentence: str) -> Dict:
        """Assess sentence alignment with COST strategic priorities"""
        assessment = {
            "excellence_promotion": 0,
            "interdisciplinary_research": 0,
            "young_researcher_empowerment": 0
        }
        
        text_lower = sentence.lower()
        
        # Excellence promotion indicators
        excellence_terms = ["excellence", "quality", "best practice", "innovation", "leadership"]
        assessment["excellence_promotion"] = min(5, sum(1 for term in excellence_terms if term in text_lower))
        
        # Interdisciplinary research indicators
        interdisciplinary_terms = ["interdisciplinary", "multidisciplinary", "cross-disciplinary", "holistic"]
        assessment["interdisciplinary_research"] = min(5, sum(2 for term in interdisciplinary_terms if term in text_lower))
        
        # Young researcher empowerment indicators
        empowerment_terms = ["empowerment", "development", "career", "mentorship", "training"]
        assessment["young_researcher_empowerment"] = min(5, sum(1 for term in empowerment_terms if term in text_lower))
        
        return assessment

    def _assess_content_quality(self, sentence: str) -> Dict:
        """Assess overall content quality metrics"""
        assessment = {
            "specificity": 0,
            "evidence_strength": 0,
            "innovation_language": 0,
            "networking_rationale": 0,
            "impact_demonstration": 0
        }
        
        # Specificity assessment
        if any(char.isdigit() for char in sentence):
            assessment["specificity"] += 2
        specific_terms = ["specifically", "precisely", "exactly", "particular"]
        assessment["specificity"] += sum(1 for term in specific_terms if term.lower() in sentence.lower())
        assessment["specificity"] = min(5, assessment["specificity"])
        
        # Evidence strength assessment
        evidence_terms = ["evidence", "demonstrate", "prove", "show", "indicate", "research shows"]
        assessment["evidence_strength"] = min(5, sum(1 for term in evidence_terms if term.lower() in sentence.lower()))
        
        # Innovation language assessment
        innovation_terms = ["innovative", "novel", "breakthrough", "cutting-edge", "revolutionary"]
        assessment["innovation_language"] = min(5, sum(1 for term in innovation_terms if term.lower() in sentence.lower()))
        
        # Networking rationale assessment
        networking_terms = ["collaboration", "network", "partnership", "synergy", "collective"]
        assessment["networking_rationale"] = min(5, sum(1 for term in networking_terms if term.lower() in sentence.lower()))
        
        # Impact demonstration assessment
        impact_terms = ["impact", "benefit", "value", "contribution", "advancement"]
        assessment["impact_demonstration"] = min(5, sum(1 for term in impact_terms if term.lower() in sentence.lower()))
        
        return assessment

    def _generate_sentence_improvements(self, sentence: str, section: str) -> List[str]:
        """Generate specific improvement recommendations for sentence"""
        improvements = []
        
        text_lower = sentence.lower()
        
        # Check for weak language
        weak_terms = ["try", "hope", "might", "could", "perhaps", "maybe"]
        if any(term in text_lower for term in weak_terms):
            improvements.append("Replace weak language with confident, assertive statements")
        
        # Check for vague terms
        vague_terms = ["some", "various", "several", "many", "different"]
        if any(term in text_lower for term in vague_terms):
            improvements.append("Replace vague quantifiers with specific numbers or ranges")
        
        # Check for innovation language
        innovation_terms = ["breakthrough", "novel", "innovative", "cutting-edge"]
        if not any(term in text_lower for term in innovation_terms) and section in ["State-of-the-art", "Impact"]:
            improvements.append("Add innovation-focused language to emphasize breakthrough potential")
        
        # Check for networking rationale
        network_terms = ["collaboration", "network", "synergy", "partnership"]
        if not any(term in text_lower for term in network_terms) and "networking" in section.lower():
            improvements.append("Strengthen networking rationale with specific collaboration benefits")
        
        # Check for evidence
        evidence_terms = ["demonstrate", "evidence", "research shows", "studies indicate"]
        if not any(term in text_lower for term in evidence_terms):
            improvements.append("Add evidence-based language to strengthen credibility")
        
        return improvements

    def _calculate_overall_sentence_score(self, analysis_result: Dict) -> float:
        """Calculate overall sentence score based on all assessments"""
        scores = []
        
        # Excellence criteria (33.3% weight)
        excellence_scores = list(analysis_result["excellence_criteria_assessment"].values())
        excellence_avg = np.mean(excellence_scores) if excellence_scores else 0
        scores.append(excellence_avg * 0.333)
        
        # Impact criteria (33.3% weight)
        impact_scores = list(analysis_result["impact_criteria_assessment"].values())
        impact_avg = np.mean(impact_scores) if impact_scores else 0
        scores.append(impact_avg * 0.333)
        
        # Implementation criteria (33.4% weight)
        implementation_scores = list(analysis_result["implementation_criteria_assessment"].values())
        implementation_avg = np.mean(implementation_scores) if implementation_scores else 0
        scores.append(implementation_avg * 0.334)
        
        return sum(scores)

def create_technical_annex_comprehensive_analysis_tab():
    """Create comprehensive technical annex analysis tab without dropdowns"""
    
    st.title("📋 Technical Annex Comprehensive Analysis")
    st.markdown("**Deep evaluation of every sentence against all COST 2025 requirements and criteria**")
    
    analyzer = TechnicalAnnexComprehensiveAnalyzer()
    
    # Analysis Plan Overview
    st.header("🗺️ Comprehensive Analysis Plan")
    
    analysis_plan = analyzer.create_comprehensive_analysis_plan()
    
    st.markdown("**Five-Phase Deep Analysis Framework:**")
    
    phases = [
        ("phase_1_document_parsing", "📄 Phase 1: Document Parsing & Structure"),
        ("phase_2_requirement_mapping", "🎯 Phase 2: Requirement Mapping"),
        ("phase_3_content_quality_assessment", "🔍 Phase 3: Content Quality Assessment"),
        ("phase_4_gap_analysis", "⚡ Phase 4: Gap Analysis"),
        ("phase_5_optimization_recommendations", "🚀 Phase 5: Optimization Recommendations")
    ]
    
    for phase_key, phase_title in phases:
        phase_data = analysis_plan[phase_key]
        
        with st.expander(phase_title):
            st.markdown("**Tasks:**")
            for task in phase_data["tasks"]:
                st.write(f"• {task}")
            
            st.markdown("**Deliverables:**")
            for deliverable in phase_data["deliverables"]:
                st.write(f"✓ {deliverable}")
    
    # Evaluation Framework Display
    st.header("📊 Complete Evaluation Framework")
    
    framework = analyzer.evaluation_framework
    
    # Technical Format Requirements
    with st.expander("📋 Technical Format Requirements"):
        st.subheader("Mandatory Sections")
        for section in framework["technical_format_requirements"]["mandatory_sections"]:
            st.write(f"• {section}")
        
        st.subheader("Format Requirements")
        format_reqs = framework["technical_format_requirements"]["format_requirements"]
        for req, value in format_reqs.items():
            st.write(f"• {req.replace('_', ' ').title()}: {value}")
    
    # Detailed Evaluation Criteria
    st.subheader("🎯 Detailed Evaluation Criteria")
    
    criteria_sections = [
        ("excellence_science_technology_networking", "🔬 Excellence in Science, Technology & Networking"),
        ("impact", "🌍 Impact"),
        ("implementation", "⚙️ Implementation")
    ]
    
    for criteria_key, criteria_title in criteria_sections:
        criteria_data = framework["evaluation_criteria_detailed"][criteria_key]
        
        with st.expander(f"{criteria_title} (Weight: {criteria_data['weight']}%, Threshold: {criteria_data['threshold']})"):
            for subcriterion, details in criteria_data["detailed_subcriteria"].items():
                st.markdown(f"**{subcriterion.replace('_', ' ').title()} (Weight: {details['weight']}%)**")
                for point in details["evaluation_points"]:
                    st.write(f"  • {point}")
    
    # Policy Compliance Requirements
    with st.expander("📜 Policy Compliance Requirements"):
        policy_reqs = framework["policy_compliance_requirements"]
        
        for policy_area, requirements in policy_reqs.items():
            st.markdown(f"**{policy_area.replace('_', ' ').title()}:**")
            for req, value in requirements.items():
                st.write(f"  • {req.replace('_', ' ').title()}: {value}")
    
    # Sample Sentence Analysis Demonstration
    st.header("🔍 Sample Sentence Analysis Framework")
    
    st.markdown("**Enter a sample sentence to see comprehensive analysis:**")
    sample_sentence = st.text_area(
        "Sample Sentence", 
        value="Our innovative network will leverage cutting-edge digital technologies to address sustainable finance challenges through interdisciplinary collaboration.",
        height=100
    )
    
    if sample_sentence:
        st.markdown("**Comprehensive Analysis Results:**")
        
        # Perform sample analysis
        analysis_result = analyzer.analyze_sentence_against_all_criteria(
            sample_sentence, "Impact related to objectives", 1
        )
        
        # Display results in organized tabs
        tab1, tab2, tab3, tab4, tab5 = st.tabs([
            "Excellence", "Impact", "Implementation", "Policy", "Quality"
        ])
        
        with tab1:
            st.subheader("Excellence Criteria Assessment")
            excellence = analysis_result["excellence_criteria_assessment"]
            for criterion, score in excellence.items():
                st.metric(f"{criterion.replace('_', ' ').title()}", f"{score}/5")
        
        with tab2:
            st.subheader("Impact Criteria Assessment")
            impact = analysis_result["impact_criteria_assessment"]
            for criterion, score in impact.items():
                st.metric(f"{criterion.replace('_', ' ').title()}", f"{score}/5")
        
        with tab3:
            st.subheader("Implementation Criteria Assessment")
            implementation = analysis_result["implementation_criteria_assessment"]
            for criterion, score in implementation.items():
                st.metric(f"{criterion.replace('_', ' ').title()}", f"{score}/5")
        
        with tab4:
            st.subheader("Policy Compliance Assessment")
            policy = analysis_result["policy_compliance_assessment"]
            for criterion, score in policy.items():
                st.metric(f"{criterion.replace('_', ' ').title()}", f"{score}/5")
        
        with tab5:
            st.subheader("Content Quality Metrics")
            quality = analysis_result["content_quality_metrics"]
            for criterion, score in quality.items():
                st.metric(f"{criterion.replace('_', ' ').title()}", f"{score}/5")
        
        # Overall Score
        st.metric("Overall Sentence Score", f"{analysis_result['overall_score']:.2f}/5")
        
        # Improvement Recommendations
        if analysis_result["improvement_recommendations"]:
            st.subheader("🎯 Improvement Recommendations")
            for recommendation in analysis_result["improvement_recommendations"]:
                st.write(f"• {recommendation}")
    
    # Implementation Roadmap
    st.header("🛣️ Implementation Roadmap")
    
    roadmap_data = {
        "Phase": ["Phase 1", "Phase 2", "Phase 3", "Phase 4", "Phase 5"],
        "Duration (Days)": [5, 10, 15, 8, 7],
        "Complexity": ["Medium", "High", "Very High", "High", "Medium"],
        "Output": [
            "Document Structure",
            "Requirement Coverage Matrix",
            "Quality Assessment Database",
            "Gap Analysis Report",
            "Optimization Strategy"
        ]
    }
    
    roadmap_df = pd.DataFrame(roadmap_data)
    st.dataframe(roadmap_df, use_container_width=True)
    
    # Visualization of analysis framework
    fig_framework = go.Figure()
    
    # Create hierarchical framework visualization
    categories = ["Excellence", "Impact", "Implementation"]
    weights = [33.3, 33.3, 33.4]
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c']
    
    fig_framework.add_trace(go.Pie(
        labels=categories,
        values=weights,
        hole=0.3,
        marker_colors=colors,
        textinfo='label+percent',
        title="COST Evaluation Criteria Weights"
    ))
    
    fig_framework.update_layout(
        title="COST 2025 Evaluation Framework",
        showlegend=True,
        height=400
    )
    
    st.plotly_chart(fig_framework, use_container_width=True)
    
    # Next Steps
    st.header("🚀 Next Steps for Full Implementation")
    
    next_steps = [
        "🔧 **Technical Setup**: Configure document parsing engine for RTF/PDF processing",
        "📊 **Database Design**: Create comprehensive sentence analysis database",
        "🤖 **AI Integration**: Enhance analysis with advanced language models",
        "📈 **Visualization Engine**: Build interactive dashboards for results",
        "🎯 **Recommendation System**: Develop AI-powered improvement suggestions",
        "⚡ **Performance Optimization**: Implement parallel processing for large documents",
        "🔍 **Quality Assurance**: Add validation and verification mechanisms"
    ]
    
    for step in next_steps:
        st.markdown(step)
    
    # Success Metrics
    st.header("📈 Success Metrics for Full Analysis")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Sentences Analyzed", "Target: 500+")
        st.metric("Requirements Checked", "Target: 150+")
    
    with col2:
        st.metric("Analysis Accuracy", "Target: >95%")
        st.metric("Processing Time", "Target: <30 min")
    
    with col3:
        st.metric("Improvement Suggestions", "Target: 100+")
        st.metric("Success Probability", "Target: >80%")

if __name__ == "__main__":
    create_technical_annex_comprehensive_analysis_tab()