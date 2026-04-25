---
id: sailfin-geared-vs-gearless
name: Sailfin Geared vs. Gearless
type: comparison
compares: [sailfin-geared, sailfin-gearless]
source_docs:
  - "Envira-North 2025__Catalogue__EN__Rev-03__11.27.2025 (pdfplumber).txt"
  - "Altra-AirSailfin_Design&Engineering_2022 (pdfplumber).txt"
  - "Altra-AirSailfinGearless_Design&Engineering_202215YearWarranty (pdfplumber).txt"
  - "EN921X8240 Altra-AirSailfin_Geared&Gearless_InstallationGuide_11142024 (pdfplumber).txt"
last_verified: 2026-04-11
---

# Sailfin Geared vs. Gearless

## TL;DR
- **Gearless** — direct-drive, no gearbox, no oil change, simpler long-term maintenance. Sizes 8/12/16/20/24 ft (gearless 8 ft does exist per the gearless D&E guide). All sizes run at **2 HP**. Noise level: **45 dBA** across all sizes. Enclosure: **IP66**.
- **Geared** — Nord Helical Inline Reducer gearmotor, requires first-start vent-plug removal and 20,000-hour oil changes. Sizes 8/12/16/20/24 ft. HP varies by size (1 HP to 2 HP). Noise level: **62.5–63.4 dBA**. Enclosure: **IP65**.

## When to choose gearless
- Long-term labour cost matters (no oil changes)
- Facility wants "install and forget" maintenance
- Noise-sensitive applications — gearless runs at 45 dBA vs. geared's 62.5–63.4 dBA
- Budget allows the higher motor cost
- Voltage supply is 230 V or 460 V (gearless voltage options are more limited)

## When to choose geared
- Up-front cost matters more than lifetime maintenance
- Facility already services gearboxes on other equipment
- Need 575 V or 400 V supply (geared supports 230/400/460/575 V; gearless supports 230/460 V only)
- Specific spec sheet SKU alignment with an existing design

## Side-by-side specs
| Item | Gearless | Geared |
|---|---|---|
| Sizes | 8 / 12 / 16 / 20 / 24 ft | 8 / 12 / 16 / 20 / 24 ft |
| Drive | Direct-drive motor (2 HP all sizes) | Nord Helical Inline Reducer gearmotor |
| Oil change | None | Every 20,000 hrs |
| First-start ritual | Standard | **Remove rubber vent plug from gearbox first** |
| HP (size-dependent) | **2 HP all sizes** | 1 HP (12 ft) / 1.5 HP (16 ft) / 2 HP (20 & 24 ft) |
| Voltage options | **230 V / 460 V only** | 230 V / 400 V / 460 V / 575 V |
| Standard power input | 208 / 230 / 400 / 460 V | 208 / 230 / 400 / 460 / 575 V |
| Noise level | **45 dBA** (all sizes) | 62.5–63.4 dBA (varies by size) |
| Enclosure (VFD) | **IP66** | **IP65** |
| Min clearance | 10 ft blade-to-floor | 10 ft blade-to-floor |
| Min speed | 15 Hz / 27 % | 15 Hz / 27 % |
| Control compatibility | Same (Schneider or Lenze path) | Same |
| Safety Clips | Yes | Yes |
| Guy Wires | 1/8" Stainless Steel (same) | 1/8" Stainless Steel (same) |
| Safety Cable | 3/16" Stainless Steel (same) | 3/16" Stainless Steel (same) |

## Detailed geared specs by size (from D&E guide)
| Size | Model No. | HP | Gear Ratio | Torque | Thrust | Max Speed | Amps @ 230V |
|---|---|---|---|---|---|---|---|
| 8 ft (2.4 m) | EN675X5002 | 1 HP (0.75 kW) | 13.39 | 53 Nm (39 ft-lbs) | 125 N (28 lbs) | 105 RPM | 3 A |
| 12 ft (3.7 m) | EN675X5006 | 1 HP (0.75 kW) | 13.39 | 53 Nm (39 ft-lbs) | 125 N (28 lbs) | 105 RPM | 3 A |
| 16 ft (4.9 m) | EN675X5010 | 1.5 HP (1.1 kW) | 23.74 | 141 Nm (104 ft-lbs) | 231 N (52 lbs) | 80 RPM | 3.6 A |
| 20 ft (6.1 m) | EN675X5014 | 2 HP (1.5 kW) | 27.24 | 217 Nm (160 ft-lbs) | 280 N (63 lbs) | 63 RPM | 5.6 A |
| 24 ft (7.3 m) | EN675X5016 | 2 HP (1.5 kW) | 30.43 | 248 Nm (183 ft-lbs) | 632 N (142 lbs) | 53 RPM | 5.7 A |

## Detailed gearless specs by size (from D&E guide)
| Size | Model No. | HP | Noise | Amps @ 230V | Max Speed |
|---|---|---|---|---|---|
| 8 ft (2.4 m) | EN670X5002 | 2 HP (1.5 kW) | 45 dBA | 5.0 A | 105 RPM |
| 12 ft (3.7 m) | EN670X5006 | 2 HP (1.5 kW) | 45 dBA | 5.0 A | 105 RPM |
| 16 ft (4.9 m) | EN670X5010 | 2 HP (1.5 kW) | 45 dBA | 5.0 A | 80 RPM |
| 20 ft (6.1 m) | EN670X5014 | 2 HP (1.5 kW) | 45 dBA | 5.0 A | 63 RPM |
| 24 ft (7.3 m) | EN670X5016 | 2 HP (1.5 kW) | 45 dBA | 5.0 A | 53 RPM |

## CFM comparison (from source)
Both geared and gearless fans of the same diameter produce the same airflow — the gear or direct-drive mechanism does not affect CFM output. Figures below apply to both:

| Size | Airflow (CFM) | Airflow (l/s) | Max Effective Diameter |
|---|---|---|---|
| 8 ft (2.4 m) | 59,494 CFM | 28,078 l/s | 60 ft (18 m) |
| 12 ft (3.7 m) | 70,424 CFM | 33,236 l/s | 80 ft (24 m) |
| 16 ft (4.9 m) | 127,033 CFM | 59,953 l/s | 140 ft (43 m) |
| 20 ft (6.1 m) | 176,200 CFM | 83,157 l/s | 200 ft (61 m) |
| 24 ft (7.3 m) | 315,026 CFM | 148,676 l/s | 230 ft (70 m) |

> Note: Maximum effective diameter is where horizontal airspeed at 1.0 ft above floor drops below 0.2 m/s in an empty room.

## Maintenance differences
- **Gearless:** visual inspection 6 months initial, then 18 months. That's it — no oil.
- **Geared:** same inspection schedule + gearbox oil check at 18 months + oil change at 20,000 hours + **never forget** the first-start vent plug removal

## Control compatibility (same for both)
Both geared and gearless can run on:
- Schneider VFD path: SmartAIR, SmartAIR Multi-Fan, TouchAIR
- Lenze VFD path: EssentialAIR, ZoneAIR, CommandAIR, ModAIR
- LVC analogue path with TFD-1 for simple temperature automation

## Construction differences
| Component | Gearless | Geared |
|---|---|---|
| Hub | 713 Cast Aluminum Alloy | 713 Cast Aluminum Alloy |
| Blades | 6063 Extruded Anodized Aluminum (D&E) / 6005-T61 Aluminum (installation guide) | 6063 Extruded Anodized Aluminum |
| Blade End Caps | High Impact Polystyrene | High Impact Polystyrene |
| Frame | — (no galvanized steel frame noted in gearless D&E) | Galvanized Steel Frame |
| Blade anodizing | 10 Microns (0.0004") clear | 10 Microns (0.0004") clear |

> Note: The installation guide specifies 6005-T61 aluminum for blades on both geared and gearless. The D&E guides specify 6063-T5. Contact Envira-North to confirm the current blade specification.

## Common FAQs

**Q: Is there an 8 ft gearless Sailfin?**
A: Yes — the Gearless D&E Guide (EN670X5002) lists an 8 ft gearless fan. However, confirm current availability with Envira-North Customer Support, as some earlier documentation lists gearless as starting at 12 ft.

**Q: Which is "better"?**
A: Neither is objectively better — it's a trade-off. Gearless is quieter (45 dBA vs. 62.5–63.4 dBA), simpler to own long-term (no oil changes), and has IP66 vs. IP65 enclosure. Geared supports more voltage options (including 575 V) and has a lower up-front cost.

**Q: Do they use the same mounting kits?**
A: The kit is matched to the size, structure, and fan version. Confirm with Envira-North Customer Support when ordering.

**Q: Can I retrofit a geared Sailfin to gearless?**
A: Not supported. The motor, hub, and drive are all matched at the factory.

## Source Documents Referenced
- `Envira-North 2025__Catalogue__EN__Rev-03__11.27.2025 (pdfplumber).txt`
- `Altra-AirSailfin_Design&Engineering_2022 (pdfplumber).txt`
- `Altra-AirSailfinGearless_Design&Engineering_202215YearWarranty (pdfplumber).txt`
- `EN921X8240 Altra-AirSailfin_Geared&Gearless_InstallationGuide_11142024 (pdfplumber).txt`
