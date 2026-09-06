BRICK = {
    "brick_num": 19,
    "brick_title": "Spectrum of Activity and Indications 2 — Beta-Lactams and 30S Inhibitors",
    "games": [
        {
            "slug": "beta_lactam_gram_negative",
            "title": "Beta-Lactams Against the Gram-Negatives",
            "subtitle": "Match each beta-lactam to its gram-negative coverage, its key gap, and its clinical pearl",
            "categories": ["Gram-Negative Coverage", "Key Gap", "Clinical Pearl"],
            "data": {
                "Amoxicillin / Ampicillin (+ beta-lactamase inhibitor)": {
                    "Gram-Negative Coverage": "Good gram-negative and atypical coverage; Neisseria meningitidis with sulbactam",
                    "Key Gap": "No ESBL-producing Enterobacteriaceae and no Pseudomonas",
                    "Clinical Pearl": "Keeps good gram-positive coverage, Enterococcus included, but not MRSA"
                },
                "Piperacillin-Tazobactam": {
                    "Gram-Negative Coverage": "Enterobacter, E. coli, Klebsiella, Serratia, Proteus, ESBLs, and Pseudomonas",
                    "Key Gap": "Broad gram-positive coverage except MRSA",
                    "Clinical Pearl": "One of the broadest coverages, so used for initial empiric therapy"
                },
                "Carbapenems": {
                    "Gram-Negative Coverage": "Covers most gram-negative bacteria, ESBL producers included",
                    "Key Gap": "Ertapenem misses Pseudomonas, Enterococci, and Acinetobacter (PEA)",
                    "Clinical Pearl": "Reserved for complicated intra-abdominal, urinary, and hospital-acquired infections"
                },
                "Monobactams": {
                    "Gram-Negative Coverage": "Aerobic gram-negative bacteria; highly resistant to their beta-lactamases",
                    "Key Gap": "Do not treat gram-positive bacteria or anaerobes",
                    "Clinical Pearl": "Treat gram-negative bacilli without disrupting the patient's microbiota"
                },
                "Nafcillin / Oxacillin": {
                    "Gram-Negative Coverage": "Not effective against many gram-negative bacteria",
                    "Key Gap": "Resistance via beta-lactamase enzymes and efflux pumps",
                    "Clinical Pearl": "Anti-staphylococcal penicillin; alternative to cephalexin for non-purulent cellulitis"
                }
            }
        },
        {
            "slug": "spectrum_niches",
            "title": "Spectrum Niches: 30S Inhibitors and Friends",
            "subtitle": "Match each agent to its gram-positive activity, gram-negative reach, and blind spots",
            "categories": ["Gram-Positive Activity", "Gram-Negative Reach", "Not Covered"],
            "data": {
                "Aminoglycosides": {
                    "Gram-Positive Activity": "Limited; used synergistically with other antibiotics",
                    "Gram-Negative Reach": "Enterobacteriaceae family plus Pseudomonas aeruginosa",
                    "Not Covered": "Anaerobic bacteria and atypical pathogens"
                },
                "Doxycycline": {
                    "Gram-Positive Activity": "Staphylococcus including MRSA, Streptococcus, Enterococcus including VRE",
                    "Gram-Negative Reach": "Acinetobacter, Legionella, Neisseria gonorrhoeae, Haemophilus influenzae",
                    "Not Covered": "Pseudomonas aeruginosa; limited activity against anaerobes"
                },
                "Ertapenem": {
                    "Gram-Positive Activity": "Broad, like other carbapenems, but not MRSA or Enterococci",
                    "Gram-Negative Reach": "Most gram-negatives, including ESBL-producing bacteria",
                    "Not Covered": "PEA: Pseudomonas, Enterococci, Acinetobacter"
                },
                "Monobactams (class)": {
                    "Gram-Positive Activity": "None — gram-positive organisms are not treated",
                    "Gram-Negative Reach": "Aerobic gram-negative bacilli, despite their beta-lactamases",
                    "Not Covered": "Gram-positives and anaerobic organisms alike"
                }
            }
        },
        {
            "slug": "drug_to_indication",
            "title": "Right Drug, Right Infection",
            "subtitle": "Match each drug to the indication the brick gives it and the organisms it targets there",
            "categories": ["Indication", "Organisms Targeted"],
            "data": {
                "Amoxicillin/Clavulanate": {
                    "Indication": "Acute bacterial sinusitis, an upper respiratory infection",
                    "Organisms Targeted": "S. pneumoniae, H. influenzae, M. catarrhalis"
                },
                "Doxycycline (as first-line)": {
                    "Indication": "First-line for Rickettsiae and Lyme's disease; atypical pneumonia",
                    "Organisms Targeted": "Mycoplasma pneumoniae, Chlamydia trachomatis, Rickettsiae"
                },
                "Cephalexin": {
                    "Indication": "Oral treatment of non-purulent cellulitis",
                    "Organisms Targeted": "S. pyogenes (Group A Strep) and S. aureus"
                },
                "Ampicillin (with or after Ceftriaxone/Vancomycin)": {
                    "Indication": "Meningitis in neonates, patients over 50, or immunocompromised",
                    "Organisms Targeted": "Listeria monocytogenes"
                },
                "Ceftriaxone with or without Vancomycin": {
                    "Indication": "Empiric coverage of bacterial meningitis in adults",
                    "Organisms Targeted": "S. pneumoniae, N. meningitidis, and H. influenzae"
                },
                "Carbapenems (as a class)": {
                    "Indication": "Hard-to-treat intra-abdominal, urinary tract, and hospital-acquired pneumonia",
                    "Organisms Targeted": "ESBL-producing bacteria that degrade other beta-lactams"
                }
            }
        }
    ]
}
