# COST 2025 Proposal Analyzer

A comprehensive Streamlit application for analyzing COST Action proposals against 2025 requirements and regulations.

## Features

### 🔍 Document Analysis
- **PDF/DOCX Upload**: Upload Technical Annex documents for analysis
- **Technical Compliance**: Check format requirements (pages, font, size, anonymity)
- **Content Quality**: AI-powered assessment of scientific excellence and innovation
- **Section Coverage**: Analyze coverage of required proposal sections

### 📊 Visualization Dashboards
- **Compliance Dashboard**: Real-time technical compliance metrics
- **Quality Assessment**: Radar charts and scoring matrices
- **Section Coverage**: Bar charts showing section completeness vs importance
- **Policy Compliance**: Visual representation of inclusiveness and equality metrics

### 🎯 Quality Assessment Framework

#### Technical Compliance (Automated)
- Page limit enforcement (15 pages max)
- File size validation (10MB max)
- Anonymity violation detection
- Format requirement verification

#### Content Quality (AI-Powered)
- **Scientific Excellence** (0-5 scale)
  - Innovation level assessment
  - Technical advancement evaluation
  - Research methodology quality
  
- **Networking Rationale** (0-5 scale)
  - Collaboration justification strength
  - Value-add demonstration
  - Geographic distribution benefits
  
- **Impact Assessment** (0-5 scale)
  - Societal impact potential
  - Economic value demonstration
  - Stakeholder engagement quality
  
- **Implementation Feasibility** (0-5 scale)
  - Timeline realism
  - Resource allocation appropriateness
  - Risk management quality

#### Section Coverage Analysis
- **State of the Art** (15% weight)
  - Literature review completeness
  - Gap identification clarity
  - Positioning accuracy
  
- **Rationale for Networking** (15% weight)
  - Collaboration necessity demonstration
  - Added value articulation
  - Complementary expertise showcase
  
- **Critical Mass** (10% weight)
  - Network size justification
  - Participant expertise coverage
  - Geographic distribution rationale
  
- **Impact Related to Objectives** (20% weight)
  - Objective clarity and measurability
  - Impact pathway demonstration
  - Stakeholder benefit articulation
  
- **Stakeholder Involvement** (15% weight)
  - Industry engagement strategy
  - End-user integration plan
  - Dissemination approach
  
- **Action Structure** (10% weight)
  - Management framework clarity
  - Governance structure appropriateness
  - Decision-making processes
  
- **Work Plan** (10% weight)
  - Task definition clarity
  - Timeline realism
  - Milestone appropriateness
  
- **Deliverables** (5% weight)
  - Output specification
  - Quality assurance measures
  - Impact measurement methods

### 📋 Evaluation Criteria (2025 Standards)

#### Excellence in Science & Technology and Networking (33.3%)
- **Threshold**: 3.0/5.0 minimum
- **Components**:
  - Scientific innovation and breakthrough potential
  - Technological advancement significance
  - Networking value demonstration
  - Interdisciplinary approach quality
  - Open science commitment

#### Impact (33.3%)
- **Threshold**: 3.0/5.0 minimum
- **Components**:
  - Societal challenge addressing
  - Economic impact potential
  - Scientific advancement contribution
  - Stakeholder engagement effectiveness
  - UN SDG alignment

#### Implementation (33.4%)
- **Threshold**: 3.0/5.0 minimum
- **Components**:
  - Project management capability
  - Timeline and milestone realism
  - Resource allocation efficiency
  - Leadership and coordination quality
  - Risk management strategy

### 🌍 Policy Compliance Requirements

#### Inclusiveness Policy
- **ITC Participation**: Minimum 50% from Inclusiveness Target Countries
- **ITC Leadership**: 50% of leadership positions reserved for ITC representatives
- **Geographic Balance**: Wide European distribution requirement

#### Gender Equality
- **Female Participation**: Target >50% across all activities
- **Gender Equality Plan**: Required within 6 months of Action start
- **GEAR Tool Usage**: Mandatory consideration and implementation

#### Young Researchers and Innovators
- **YRI Participation**: Minimum 50% overall participation
- **YRI Leadership**: 45% of leadership positions allocated
- **Mentorship Programs**: Structured support and development

### 🔧 Technical Requirements (2025)

#### Format Specifications
- **Maximum Pages**: 15 pages (strictly enforced)
- **Font**: Arial, size 10, line spacing 1
- **File Format**: Single PDF document
- **File Size**: Maximum 10MB
- **Template**: Mandatory new Technical Annex template for oc-2025-1

#### Submission Requirements
- **Platform**: e-COST online system only
- **Deadline**: October 21, 2025, 12:00 noon (CEST)
- **Anonymity**: Complete removal of identifying information
- **Language**: English only

### 📈 Scoring and Recommendations

#### Overall Quality Score Calculation
```
Technical Compliance (20%) + 
Content Quality (40%) + 
Section Coverage (25%) + 
Policy Alignment (15%) = 
Total Score (0-100%)
```

#### Recommendation Engine
- **High Priority**: Technical compliance violations, scoring below thresholds
- **Medium Priority**: Section coverage gaps, policy alignment issues
- **Low Priority**: Style improvements, optimization suggestions

## Installation and Setup

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation Steps

1. **Clone or download the application files**

2. **Install required packages**
```bash
pip install -r requirements.txt
```

3. **Configure OpenAI API Key**
   - Edit `.streamlit/secrets.toml`
   - Replace `"your-openai-api-key-here"` with your actual OpenAI API key
   - For enhanced AI analysis features (optional but recommended)

4. **Run the application**
```bash
streamlit run cost_analyzer_app.py
```

5. **Access the application**
   - Open your web browser
   - Navigate to `http://localhost:8501`

### Configuration Options

#### OpenAI Integration
- **Required for**: Advanced content quality analysis
- **Models used**: GPT-4o for comprehensive text analysis
- **Cost**: Approximately $0.01-0.05 per analysis (depending on document length)

#### Offline Mode
- **Technical compliance**: Fully functional offline
- **Section coverage**: Pattern-based analysis (offline)
- **Content quality**: Limited to rule-based analysis without OpenAI

## Usage Guide

### Basic Analysis Workflow

1. **Upload Document**
   - Select "Document Upload & Analysis" from sidebar
   - Upload your Technical Annex (PDF or DOCX)
   - Wait for processing completion

2. **Review Compliance Tab**
   - Check technical format compliance
   - Address any red-flag issues immediately
   - Verify file size and page count

3. **Analyze Quality Tab**
   - Review AI-powered quality scores
   - Read detailed justifications
   - Identify improvement areas

4. **Examine Coverage Tab**
   - Check section completeness
   - Focus on high-weight sections
   - Ensure balanced coverage

5. **Follow Recommendations Tab**
   - Prioritize high-priority recommendations
   - Address compliance issues first
   - Implement content improvements

### Advanced Features

#### Comparative Analysis
- Upload multiple versions for progress tracking
- Compare against successful proposals
- Historical improvement visualization

#### Export and Reporting
- Generate comprehensive analysis reports
- Export data for external processing
- Share results with team members

## Best Practices for High-Quality Proposals

### Content Strategy
1. **Start with strong state-of-the-art**: Comprehensive literature review demonstrating clear gaps
2. **Emphasize networking value**: Show why collaboration is essential, not just convenient
3. **Quantify impact**: Use specific metrics and measurable outcomes
4. **Balance sections**: Allocate content proportional to evaluation weights

### Technical Optimization
1. **Use official template**: Download latest template from e-COST platform
2. **Check formatting early**: Run compliance checks throughout writing process
3. **Maintain anonymity**: Remove all identifying information from early drafts
4. **Optimize file size**: Use compressed images and efficient formatting

### Policy Integration
1. **Plan inclusiveness**: Ensure meaningful ITC participation from project start
2. **Embed gender equality**: Integrate throughout proposal, not as afterthought
3. **Highlight young researchers**: Show concrete development opportunities
4. **Engage stakeholders**: Demonstrate real industry and policy connections

## Technical Architecture

### Core Components
- **Document Parser**: PDF/DOCX text extraction
- **Compliance Engine**: Rule-based format validation
- **AI Analyzer**: OpenAI-powered content assessment
- **Visualization Engine**: Plotly-based interactive charts
- **Recommendation System**: Multi-criteria decision support

### Performance Optimization
- **Caching**: Streamlit session state for repeated analyses
- **Chunking**: Large document processing in segments
- **Async Processing**: Background analysis for responsive UI

## Troubleshooting

### Common Issues

#### "Error reading PDF"
- **Cause**: Corrupted or protected PDF file
- **Solution**: Re-save PDF or use DOCX format

#### "AI analysis failed"
- **Cause**: OpenAI API key not configured or quota exceeded
- **Solution**: Check secrets.toml configuration or account limits

#### "File too large"
- **Cause**: Document exceeds 10MB limit
- **Solution**: Compress images or optimize document structure

### Performance Tips
- **Document Size**: Keep under 5MB for optimal processing speed
- **Internet Connection**: Stable connection required for AI analysis
- **Browser**: Use Chrome or Firefox for best compatibility

## Future Enhancements

### Planned Features
- **Multi-language Support**: Analysis of non-English proposals
- **Template Generation**: Automated proposal structure creation
- **Collaboration Tools**: Team review and comment features
- **Integration APIs**: Connect with external proposal management systems

### Advanced Analytics
- **Success Prediction**: Machine learning models for approval probability
- **Competitive Analysis**: Benchmarking against successful proposals
- **Trend Analysis**: Historical success factor identification

## Support and Contact

For technical support or feature requests:
- Create issue reports with detailed error descriptions
- Include sample documents (anonymized) for reproduction
- Specify browser and operating system information

## License and Usage Rights

This tool is designed for educational and research purposes. Users are responsible for:
- Maintaining confidentiality of sensitive proposal content
- Compliance with institutional data policies
- Appropriate use of AI analysis features

---

**Last Updated**: July 2025  
**Version**: 1.0.0  
**Compatibility**: COST 2025 Requirements (oc-2025-1)