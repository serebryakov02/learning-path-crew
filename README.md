# Learning Path Crew

This project uses CrewAI to generate a practical learning path for a topic. It researches useful resources, turns them into a week-by-week study plan, and writes the results to the `output/` directory.

## Run locally

1. Install Python 3.10 to 3.12 and `uv`.
2. Install dependencies:

```bash
uv sync
```

3. Add your `OPENAI_API_KEY` to a `.env` file in the project root.
4. Set the topic you want to plan for in `src/learning-path-crew/main.py`.
5. Run the crew from the project root:

```bash
crewai run
```

Generated files are written to:

- `output/resources.md`
- `output/learning_plan.md`
- `output/final_guide.md`
