# Scraped Wiki JSON format (style reference)

This skill uses a scraped product wiki JSON as a **style/structure reference** (page taxonomy and writing patterns), not as the factual source for the current repo.

It expects a JSON object like:

```json
{
  "wiki": {
    "wikis": {
      "en": {
        "metadata": { "...": "..." },
        "pages": [
          {
            "page_plan": { "id": "1", "title": "Overview" },
            "content": "# Overview\n\n..."
          }
        ]
      }
    }
  }
}
```

## Fields

- `wiki.wikis`: map of language code → wiki bundle
- `wiki.wikis[lang].pages[]`: ordered list of pages
- `page_plan.id`: ordering key (string like `1`, `2.4`, `3.1`)
- `page_plan.title`: human title
- `content`: Markdown content for the page

## Notes

- Not all datasets contain all languages. If the target language is missing, you can still use any available language to infer structure/tone.
- Avoid copying large verbatim passages from the scraped content unless the user confirms they have rights; mimic structure/tone and write new, repo-grounded text.
