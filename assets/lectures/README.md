# Lecture deck renders

This directory contains page-faithful website renders of the 11 ETH Robot Learning lecture decks. Redistribution permission was confirmed for this repository. The slide content retains the copyright and reuse terms of the source decks and is not covered by the repository's MIT license.

| Week | Source filename | Slides |
| ---: | --- | ---: |
| 1 | `lecture1_intro.pdf` | 44 |
| 2 | `lecture2_control_mdp.pdf` | 46 |
| 3 | `lecture3_imitation.pdf` | 45 |
| 4 | `lecture4_rl_I.pdf` | 45 |
| 5 | `lecture5_rl_II.pdf` | 36 |
| 6 | `lecture6_generative.pdf` | 39 |
| 7 | `lecture7_sequence_modeling.pdf` | 39 |
| 8 | `lecture8_world_models.pdf` | 55 |
| 9 | `lecture9_generalist_policies.pdf` | 59 |
| 10 | `lecture10_reasoning.pdf` | 57 |
| 11 | `lecture11_frontiers.pdf` | 50 |

The images are progressive JPEGs rendered at 1600 pixels wide. Rebuild them with [`scripts/render_lecture_decks.sh`](../../scripts/render_lecture_decks.sh); pass the password through the `PDF_PASSWORD` environment variable and never commit it.
