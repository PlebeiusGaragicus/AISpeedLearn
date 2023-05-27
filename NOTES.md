# prompt

```json
{
    "documents": [
        {
            "sectionTitle": "",
            "sectionText": ""
        }
    ],
    "instruction": "Create study flashcards from the given text document. Provide no extra dialogue - only Q/A pairs. Answers should be short (1-6) words. Create multiple flashcards as needed for longer sentences."
}
```


# Notes on the data...

OG 2.15 has nonstandard formatting and needs to be manually adjusted

OG 1.3:
- has a section with a photo (which we aren't processing)
- last section is a data table (which we don't want the AI to make flashcards for)
