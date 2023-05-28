# Use workflow

0. Copy all desired review documents into the `./dataset/source_documents`

1. **Extract** the text out of the source documents

```sh
./tools/extract_text
```

This will generate text documents into the `./dataset/extracted` folder.

2. Run AI models to process into 'study' format

```sh
aisl s
```

3. Run self-hosted web app to study these materials
