BRICK = {
    "brick_num": 14,
    "brick_title": "Spectrum of Activity and Indications 1 — Beta-Lactams and Vancomycin",
    "games": [
        {
            "slug": "penicillin_spectrum",
            "title": "Penicillin Family: Who Covers What",
            "subtitle": "Match each penicillin to its spectrum, classic use, and resistance note",
            "categories": ["Spectrum of activity", "Classic use or indication", "Resistance note"],
            "data": {
                "Penicillin VK": {
                    "Spectrum of activity": "Gram-positive cocci: Staphylococci and some Streptococci",
                    "Classic use or indication": "First-line oral agent for streptococcal pharyngitis",
                    "Resistance note": "Many Gram-positive organisms have developed resistance to it"
                },
                "Nafcillin": {
                    "Spectrum of activity": "Susceptible (methicillin-sensitive) Staphylococcus aureus strains",
                    "Classic use or indication": "Developed specifically to overcome staphylococcal resistance",
                    "Resistance note": "MRSA strains are not susceptible to this antistaphylococcal drug"
                },
                "Amoxicillin": {
                    "Spectrum of activity": "Broad-spectrum: good Gram-positive and Gram-negative coverage",
                    "Classic use or indication": "First-line for otitis media due to Strep pneumoniae",
                    "Resistance note": "Clavulanic acid can be added to defeat beta-lactamases"
                },
                "Piperacillin-Tazobactam": {
                    "Spectrum of activity": "Very broad: Gram-positives, Gram-negatives, and anaerobes",
                    "Classic use or indication": "Antipseudomonal penicillin, effective against Pseudomonas aeruginosa",
                    "Resistance note": "Tazobactam protects piperacillin from beta-lactamase degradation"
                }
            }
        },
        {
            "slug": "cephalosporin_generations",
            "title": "Cephalosporins by Generation",
            "subtitle": "Match each cephalosporin to its generation, coverage, and high-yield point",
            "categories": ["Generation", "Spectrum of activity", "High-yield point"],
            "data": {
                "Cephalexin": {
                    "Generation": "First generation (the oral agent)",
                    "Spectrum of activity": "Mostly Gram-positives: Staph aureus and Streptococcus species",
                    "High-yield point": "Used for uncomplicated skin and soft tissue infections"
                },
                "Cefoxitin": {
                    "Generation": "Second generation",
                    "Spectrum of activity": "Limited Gram-positive coverage, more effective against Gram-negatives",
                    "High-yield point": "With cefotetan, one of two cephalosporins covering Bacteroides"
                },
                "Ceftriaxone": {
                    "Generation": "Third generation",
                    "Spectrum of activity": "Broad Gram-positive plus extended Gram-negative coverage",
                    "High-yield point": "Covers Neisseria meningitidis and Neisseria gonorrhoeae"
                },
                "Cefepime": {
                    "Generation": "Fourth generation",
                    "Spectrum of activity": "Good Gram-positive coverage with even more Gram-negative reach",
                    "High-yield point": "Retains Gram-positive activity but still misses MRSA"
                },
                "Ceftaroline": {
                    "Generation": "Fifth generation",
                    "Spectrum of activity": "Broad-spectrum activity that includes Gram-negative bacteria",
                    "High-yield point": "The cephalosporin notable for activity against MRSA"
                }
            }
        },
        {
            "slug": "first_line_picks",
            "title": "Pick the First-Line Agent",
            "subtitle": "Match each infection to its first-line antibiotic and the reason it fits",
            "categories": ["First-line antibiotic", "Why that drug fits"],
            "data": {
                "Streptococcal pharyngitis": {
                    "First-line antibiotic": "Oral penicillin (Penicillin VK)",
                    "Why that drug fits": "Strep species remain treatable with a first-line oral penicillin"
                },
                "Otitis media": {
                    "First-line antibiotic": "Amoxicillin, with or without clavulanic acid",
                    "Why that drug fits": "Covers Strep pneumoniae and susceptible Gram-negative bacteria"
                },
                "Uncomplicated skin and soft tissue infection": {
                    "First-line antibiotic": "First-generation cephalosporin such as cephalexin",
                    "Why that drug fits": "Gram-positive cocci typically cause these infections"
                },
                "Surgical prophylaxis through the skin": {
                    "First-line antibiotic": "Cefazolin",
                    "Why that drug fits": "IV dosing gives rapid peak tissue levels at incision time"
                },
                "MRSA infection": {
                    "First-line antibiotic": "Vancomycin or ceftaroline",
                    "Why that drug fits": "Few antibiotics remain effective once methicillin resistance develops"
                },
                "C. difficile infection": {
                    "First-line antibiotic": "Vancomycin given orally",
                    "Why that drug fits": "Unabsorbed oral drug acts topically in the gastric mucosa"
                }
            }
        },
        {
            "slug": "tough_bugs_coverage",
            "title": "Tough Bugs and Coverage Gaps",
            "subtitle": "Match each hard-to-treat organism to its effective option and resistance fact",
            "categories": ["Effective option from this brick", "Resistance fact"],
            "data": {
                "MRSA": {
                    "Effective option from this brick": "Vancomycin and fifth-generation ceftaroline",
                    "Resistance fact": "Not susceptible to antistaphylococcal penicillins like nafcillin"
                },
                "Vancomycin-resistant Enterococcus (VRE)": {
                    "Effective option from this brick": "None named here; vancomycin no longer works",
                    "Resistance fact": "Enterococcus strains that developed resistance to vancomycin"
                },
                "Enterococcus species": {
                    "Effective option from this brick": "No cephalosporin of any generation covers them",
                    "Resistance fact": "Known for intrinsic resistance to cephalosporins"
                },
                "Bacteroides species": {
                    "Effective option from this brick": "Second-generation cefoxitin or cefotetan",
                    "Resistance fact": "Most cephalosporins do not cover these anaerobes well"
                },
                "Pseudomonas aeruginosa": {
                    "Effective option from this brick": "Piperacillin-tazobactam, the antipseudomonal penicillin",
                    "Resistance fact": "Makes beta-lactamases; tazobactam shields piperacillin from them"
                }
            }
        }
    ]
}
