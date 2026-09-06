BRICK = {
    "brick_num": 20,
    "brick_title": "Protein Synthesis Inhibitors — 1 of 2: Mechanisms of Action",
    "games": [
        {
            "slug": "ribosome_targets",
            "title": "Who Binds What on the Ribosome",
            "subtitle": "Match each class to its ribosomal target, its action, and whether it is static or cidal",
            "categories": ["Subunit Targeted", "Mechanism at the Ribosome", "Static or Cidal"],
            "data": {
                "Tetracyclines": {
                    "Subunit Targeted": "30S subunit",
                    "Mechanism at the Ribosome": "Reversibly block aminoacyl tRNA access to the A site",
                    "Static or Cidal": "Bacteriostatic (binding is reversible)"
                },
                "Aminoglycosides": {
                    "Subunit Targeted": "30S subunit, targeting the 16S rRNA",
                    "Mechanism at the Ribosome": "Cause mRNA misreading and mistranslated, nonfunctional proteins",
                    "Static or Cidal": "Bactericidal; mistranslated proteins lyse the cell membrane"
                },
                "Macrolides and clindamycin": {
                    "Subunit Targeted": "50S subunit",
                    "Mechanism at the Ribosome": "Reversibly inhibit transpeptidation and translocation across A, P, E sites",
                    "Static or Cidal": "Mostly bacteriostatic; incomplete proteins released"
                },
                "Linezolid": {
                    "Subunit Targeted": "23S rRNA of the 50S subunit, at the 30S-50S interphase",
                    "Mechanism at the Ribosome": "Prevents initiation complex formation, blocking the first peptide bond",
                    "Static or Cidal": "Unique site keeps it free of cross-resistance"
                },
                "Streptogramins (dalfopristin/quinupristin)": {
                    "Subunit Targeted": "50S subunit, both partners",
                    "Mechanism at the Ribosome": "Synergistic block of early (dalfopristin) and late (quinupristin) synthesis",
                    "Static or Cidal": "Combined action disrupts peptide chains, leading to cell death"
                },
                "Chloramphenicol": {
                    "Subunit Targeted": "50S subunit",
                    "Mechanism at the Ribosome": "Prevents transpeptidation by peptidyl transferase",
                    "Static or Cidal": "Bacteriostatic action"
                }
            }
        },
        {
            "slug": "drug_to_class",
            "title": "Name That PSI Class",
            "subtitle": "Match each drug to its class and the ribosomal subunit it inhibits",
            "categories": ["Drug Class", "Ribosomal Subunit"],
            "data": {
                "Gentamicin": {
                    "Drug Class": "Aminoglycoside (amino sugars on an aminocyclitol nucleus)",
                    "Ribosomal Subunit": "30S inhibitor, like streptomycin and amikacin"
                },
                "Doxycycline": {
                    "Drug Class": "Second-generation tetracycline ('-cycline' suffix)",
                    "Ribosomal Subunit": "30S inhibitor developed after resistance to older agents"
                },
                "Azithromycin": {
                    "Drug Class": "Macrolide, with clarithromycin and erythromycin",
                    "Ribosomal Subunit": "50S inhibitor of protein elongation"
                },
                "Clindamycin": {
                    "Drug Class": "Lincosamide",
                    "Ribosomal Subunit": "50S inhibitor sharing the macrolide target site"
                },
                "Linezolid": {
                    "Drug Class": "Oxazolidinone",
                    "Ribosomal Subunit": "50S inhibitor binding its 23S rRNA"
                },
                "Dalfopristin/quinupristin": {
                    "Drug Class": "Streptogramins used together",
                    "Ribosomal Subunit": "50S inhibitors acting synergistically"
                }
            }
        },
        {
            "slug": "resistance_mechanisms",
            "title": "How Bacteria Fight Back",
            "subtitle": "Match each drug class to the resistance mechanism the lecture pairs with it",
            "categories": ["Resistance Mechanism", "How It Works"],
            "data": {
                "Aminoglycosides": {
                    "Resistance Mechanism": "Enzymatic inactivation, spread by gram-negative organisms",
                    "How It Works": "Acetylation of the drug prevents interaction with 16S rRNA"
                },
                "Tetracyclines": {
                    "Resistance Mechanism": "Efflux by the TetA pump protein",
                    "How It Works": "Membrane antiport pumps drug out while protons flow in"
                },
                "Macrolides (MLS family)": {
                    "Resistance Mechanism": "Target site alteration via transferable erm genes",
                    "How It Works": "Methylation of 23S rRNA lowers ribosome affinity for the whole family"
                },
                "Linezolid": {
                    "Resistance Mechanism": "Largely escapes cross-resistance",
                    "How It Works": "Its unique 23S binding site deters shared resistance"
                }
            }
        },
        {
            "slug": "psi_pharmacokinetics",
            "title": "PSI Pharmacokinetics",
            "subtitle": "Match each drug or class to how it is given, where it goes, and how it leaves",
            "categories": ["Administration", "Distribution", "Elimination"],
            "data": {
                "Aminoglycosides": {
                    "Administration": "IV or IM only; very hydrophilic with poor oral absorption",
                    "Distribution": "Low protein binding, water soluble, minimal CSF penetration",
                    "Elimination": "Eliminated unchanged by the kidneys; monitor serum creatinine"
                },
                "Tetracyclines": {
                    "Administration": "Oral, IV, or IM",
                    "Distribution": "Great tissue penetration owing to lipophilicity",
                    "Elimination": "Biliary excretion in urine and feces"
                },
                "Macrolides": {
                    "Administration": "Oral bioavailability 30% to 50%, depending on gastric pH stability",
                    "Distribution": "Concentrate in tissues and phagocytic cells; poor CSF without meningeal inflammation",
                    "Elimination": "Hepatically metabolized like other 50S inhibitors"
                },
                "Clindamycin": {
                    "Administration": "About 90% bioavailability after oral dosing",
                    "Distribution": "Distributes well into body tissues, especially bone; little CSF",
                    "Elimination": "Hepatic metabolism, relevant to later drug interactions"
                },
                "Linezolid": {
                    "Administration": "Excellent oral bioavailability",
                    "Distribution": "Readily enters the CSF",
                    "Elimination": "Metabolized hepatically as a 50S ribosome-inhibiting antibiotic"
                }
            }
        }
    ]
}
