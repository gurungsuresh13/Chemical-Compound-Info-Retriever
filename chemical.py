import pubchempy as pcp
from IPython.display import Image, display

def get_compound_info(chemical_formula):
    try:
        compounds = pcp.get_compounds(chemical_formula, 'formula')
        if compounds:
            compound = compounds[0]
            print(f"Name: {compound.iupac_name}")
            print(f"Common Name: {compound.synonyms[0] if compound.synonyms else 'N/A'}")
            molecular_weight = float(compound.molecular_weight) if compound.molecular_weight else 0
            print(f"Molecular Weight: {molecular_weight:.2f}")
            print(f"Formula: {compound.molecular_formula}")
            return compound
        else:
            print(f"No information found for {chemical_formula}.")
            return None
    except pcp.PubChemHTTPError as e:
        print(f"HTTP Error: {e}")
    except ConnectionError:
        print("There was a connection error. Please check your internet connection.")
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def get_compound_image(compound, filename="compound.png"):
    try:
        pcp.download('PNG', filename, compound.cid, 'cid', overwrite=True)
        print(f"Image saved as {filename}")
    except Exception as e:
        print(f"An error occurred while downloading the image: {e}")

def display_compound_image(filename):
    display(Image(filename))

def main():
    chemical_formula = input("Enter chemical Formula: ")
    compound = get_compound_info(chemical_formula)
    if compound:
        filename = f"{chemical_formula}.png"
        get_compound_image(compound, filename=filename)
        # The following line is meant for Jupyter Notebook or IPython only.
        # For a script, you would open the PNG file manually.
        display_compound_image(filename)

if __name__ == "__main__":
    main()
