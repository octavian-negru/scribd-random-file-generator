# random-file-generator
Generates a random file of random size, with random content, grouped by random words of random length.

## The rationale of writing this script

Whenever you want to download something from Scribd and you use a free Scribd account, you are required to upload some files.

Oftentimes, the files are already present in Scribd.

The workaround is to generate random files which tricks the Scribd control.

This project gets past the Scribd control, allowing you to upload dummy files, in order to download wanted files.


## How to run

### Prerequisites

- [uv](https://docs.astral.sh/uv/getting-started/installation/) — Python package manager
- [just](https://just.systems/man/en/packages.html) — command runner

### Quickstart

```sh
just
```

This installs dependencies and runs the script in one step.

### Manual steps

Install dependencies:

```sh
just install
```

Run the script:

```sh
just run
```

Five random PDF files will be generated in the current directory.

### Good luck!
