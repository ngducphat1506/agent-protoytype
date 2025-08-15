# Pain Point to Solution Agent Prototype

## 1. Agent Input Structure 
```json
{
  "pain_point": "string (required, free-text description of the issue)",
  "industry": "string (optional)",
  "company_size": "string (optional)",
  "current_tools": "string (optional)"
}  
```
Example:
```json
{
  "pain_point": "We're struggling to collect customer feedback consistently after a purchase.",
  "industry": "Retail",
  "company_size": "Medium",
  "current_tools": "Manual email surveys"
}
```
#### Rationale
- pain_point: Captures the core issue in free-text form, enabling flexible user input for matching against features.
- Optional fields (industry, company_size, current_tools): Provide context to refine suggestions .
- JSON format: Ensures structured input, easy parsing in Python, and compatibility with future integrations.

## 2. Agent Output Structure
```json
{
  "suggested_solutions": [
    {
      "feature_name": "string (name of the Filum.ai feature)",
      "category": "string (product category, eg: VoC - Surveys)",
      "how_it_helps": "string (brief description of how the feature addresses the pain point)",
      "relevance_score": "integer (0-100, indicating match confidence)",
      "more_info_link": ["string (URLs to feature documentation)"]
    }
  ],
  "summary": "string"
}
```
#### Rationale
- `suggested_solutions` array: Allows multiple relevant features to be returned, sorted by `relevance_score` for prioritization.
- Fields per solution:
  - `feature_name` and `category` clearly identify the feature.
  - `how_it_helps` explains the solution's value.
  - `relevance_score` quantifies match quality.
  - `more_info_link` (array) supports multiple documentation links for flexibility.
- summary: Provides a concise overview for user understanding.

## 3. Core Logic & Matching Approach

The agent processes input through the following steps:
1. Parse Input: Extract `pain_point` from JSON input, ignoring optional fields for simplicity.
2. Load Knowledge Base: Read `features.json` into memory.
3. Tokenize Pain Point: Convert `pain_point` to lowercase and split into tokens (words).
4. Match Features:
- For each feature in `features.json`:
  - Combine `keywords` and `pain_points_addressed` (lowercase) into a set of tokens.
  - Count matching tokens between `pain_point` and feature tokens.
  - Calculate `relevance_score` as the percentage of matching tokens relative to `pain_point` length.
- Filter features with `relevance_score` > 20% (threshold).
5. Sort Results: Sort filtered features by `relevance_score` (descending).
6. Generate Output: Create JSON output with `suggested_solutions` and a static `summary`.

## Usage
Run the agent via command line with JSON input:

```bash
echo '{"pain_point": "your pain point here"}' | python agent_prototype.py
```

## Example

### Input
```bash
echo '{"pain_point": "We are struggling to collect customer feedback consistently"}' | python agent_prototype.py
```

### Output
```json
{
  "suggested_solutions": [
    {
      "feature_name": "Automated Post-Purchase Surveys",
      "category": "VoC - Surveys",
      "how_it_helps": "Trigger surveys automatically via email/SMS after a transaction to gather consistent feedback.",
      "relevance_score": 50,
      "more_info_link": [
        "https://filum.ai/en/products/voice-of-customer/survey"
      ]
    },
    {
      "feature_name": "Customer Journey Experience Analysis",
      "category": "Insights - Experience",
      "how_it_helps": "Identifies friction points by analyzing feedback and operational data across the journey.",
      "relevance_score": 25,
      "more_info_link": [
        "https://filum.ai/en/products/insights/topic-analysis"
      ]
    }
  ],
  "summary": "Các giải pháp phù hợp cho vấn đề của bạn."
}
```

## Sample Pain Points
Test the agent with these common business challenges:

1. Customer Feedback Collection
```bash
echo '{"pain_point": "We are struggling to collect customer feedback consistently after a purchase"}' | python agent_prototype.py
```

2. Support Agent Workload
```bash
echo '{"pain_point": "Our support agents are overwhelmed by repetitive questions"}' | python agent_prototype.py
```

3. Customer Journey Analysis
```bash
echo '{"pain_point": "We have no clear idea which customer touchpoints cause frustration"}' | python agent_prototype.py
```

4. Customer Interaction History
```bash
echo '{"pain_point": "It is difficult to get a single view of customer interaction history"}' | python agent_prototype.py
```

5. Survey Analysis
```bash
echo '{"pain_point": "Manually analyzing thousands of open-ended survey responses is time-consuming"}' | python agent_prototype.py
```

## Project Structure
- `agent_prototype.py` - Main script that processes pain points and matches solutions
- `features.json` - Knowledge base of Filum.ai features and capabilities


