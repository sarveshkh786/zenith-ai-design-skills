# 🎨 Zenith AI Design Skills

**Authored by Sarvesh Zenith (Sarvesh Khandelwal) | Dayal Infotech Services**

A curated collection of prompt designs, agent behavioral patterns, structural design guidelines, and design principles tailored for production-grade LLM applications and agentic workflows.

---

## 💡 Overview

Designing reliable AI systems requires clean patterns for prompt composition, structured JSON/schema generation, system role boundaries, and multi-agent dialogue orchestration.

`zenith-ai-design-skills` provides reusable patterns and Python/TypeScript utilities to streamline AI UI/UX and LLM behavioral architecture.

---

## 🛠 Features & Patterns

- **Structured System Guidelines**: Standardized system prompts for analytical, coding, and conversational agents.
- **Output Parsing & Guardrails**: Schema definitions and validation patterns ensuring reliable output format adherence.
- **Agentic Persona Specifications**: Modular skill templates for data science, security analysis, and cloud architecture.

---

## 🚀 Quick Example (Python)

```python
from design_skills import SkillRegistry, AgentPersona

registry = SkillRegistry()
architect = AgentPersona(name="Zenith-Architect", domain="AI Systems Architecture")

print(registry.format_prompt(architect))
```
