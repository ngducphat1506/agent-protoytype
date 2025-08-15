# Pain Point to Solution Agent Prototype
  

## Usage
Run the agent via command line with JSON input:

```bash
echo '{"pain_point": "your pain point here"}' | python agent.py
```

## Example

### Input
```bash
echo '{"pain_point": "We are struggling to collect customer feedback consistently"}' | python agent.py
```

### Output
```json
{
  "suggested_solutions": [
    {
      "feature_name": "Automated Post-Purchase Surveys",
      "category": "VoC - Surveys",
      "how_it_helps": "Trigger surveys automatically via email/SMS after a transaction to gather consistent feedback.",
      "relevance_score": 95,
      "more_info_link": ["https://filum.ai/en/products/voice-of-customer/survey"]
    }
  ],
  "summary": "Các giải pháp phù hợp cho vấn đề của bạn."
}
```

## Sample Pain Points
Test the agent with these common business challenges:

1. Customer Feedback Collection
```bash
echo '{"pain_point": "We are struggling to collect customer feedback consistently after a purchase"}' | python agent.py
```

2. Support Agent Workload
```bash
echo '{"pain_point": "Our support agents are overwhelmed by repetitive questions"}' | python agent.py
```

3. Customer Journey Analysis
```bash
echo '{"pain_point": "We have no clear idea which customer touchpoints cause frustration"}' | python agent.py
```

4. Customer Interaction History
```bash
echo '{"pain_point": "It is difficult to get a single view of customer interaction history"}' | python agent.py
```

5. Survey Analysis
```bash
echo '{"pain_point": "Manually analyzing thousands of open-ended survey responses is time-consuming"}' | python agent.py
```

## Project Structure
- `agent.py` - Main script that processes pain points and matches solutions
- `features.json` - Knowledge base of Filum.ai features and capabilities


