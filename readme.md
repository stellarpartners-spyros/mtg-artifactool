# MTG Artifactool

A tool to convert Magic: The Gathering decklists between different formats, specifically from Moxfield to Cardmarket.

## Setup

1. Clone this repository
2. Ensure you have Python 3.x installed

## Usage

1. Create a `moxfield-list.txt` file in the root directory with your decklist exported from Moxfield
2. Run the conversion script:
   ```bash
   python scripts/run-moxfield-to-cardmarket.py
   ```
3. Find your converted list in `cardmarket-list.txt`

## File Format Examples

### Moxfield Input Format
```
1 Jarad, Golgari Lich Lord (GK1) 65
1 Arcane Signet (MIC) 157
1 Birds of Paradise (RVR) 133
```

### Cardmarket Output Format
```
1 Jarad, Golgari Lich Lord (Guilds of Ravnica: Guild Kits)
1 Arcane Signet (Midnight Hunt Commander)
1 Birds of Paradise (Ravnica Remastered)

## Expansion Mappings
The tool uses a CSV file (library/expansions.csv) to map set codes to their full names. The format is:

## Contributing
Feel free to submit issues and pull requests for any improvements or bug fixes.

## License
MIT License
