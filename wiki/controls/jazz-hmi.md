---
id: jazz-hmi
name: Jazz Fan HMI (single-fan)
type: control
category: hmi
vfd: none
location: wall-mount
fans_controlled: 1
included_with: jazz-fan
works_with: [jazz-fan]
source_docs:
  - "EN561X8455 Jazz_Installation Guide_EN__Rev-03__05.29.2025 (pdfplumber).txt"
  - "JazzDesign&EngineeringGuide-Updated10.18.2024 (pdfplumber).txt"
  - "JazzBrochure_2019Mockup (pdfplumber).txt"
  - "Control Options (2023)__Brochure_EN__Rev-01__03.04.2023 (pdfplumber).txt"
last_verified: 2026-04-11
version: "2025-05"
version_source: "EN561X8455 Jazz_Installation Guide_EN__Rev-03__05.29.2025 (pdfplumber).txt"
supersedes: null
---

# Jazz Fan HMI (single-fan)

## Overview
The Jazz Fan HMI is the HMI that ships included with every Jazz Fan. It controls one Jazz Fan over a 100 ft CAT-5 communication cable. Jazz fans must be on their own network and cannot be mixed with Altra-Air Sailfin controls (SmartAIR, TouchAIR, LVC) on the same line — they have their own dedicated HMI family.

## Key Specifications
| Item | Value |
|---|---|
| Fans controlled | 1 |
| Bundled with | Jazz Fan (not sold separately as a standalone SKU in the source docs) |
| Communication cable | 100 ft CAT-5 |
| Works with | Jazz Fan only |
| Jazz LED control | Yes (dimming supported — the Jazz LED is integrated dimmable, 1,980 lumens) |

## Best Applications
- Every single-fan Jazz installation
- Commercial, residential, and institutional Jazz installs where only one fan is needed

## HMI Button Layout
| Control | Function |
|---|---|
| Bottom-left toggle button | Toggles the screen between "Fan" mode and "Light" mode |
| When screen shows "Fan" | All remaining buttons control the fan |
| When screen shows "Light" | All remaining buttons control the LED light |
| Fan Forward / Reverse | Toggles fan rotation direction |
| Speed Up / Brightness Up | Increases fan speed (Fan mode) or LED brightness (Light mode) |
| Speed Down / Brightness Down | Decreases fan speed (Fan mode) or LED brightness (Light mode) |
| On/Off | Turns fan (or light) on or off |
| Digital Display | Shows current mode (Fan/Light), speed level, or brightness level |

- The HMI remembers the last speed and light values; when the fan is turned back on it automatically resumes those settings.

## Key Features & Benefits
- Included with the fan at no extra charge
- 100 ft CAT-5 cable included
- On-board controls for start/stop, speed (0–120 RPM), LED on/off, LED dimming (20 brightness levels)
- Plug-and-play connection to the Jazz Fan's pre-wired motor assembly
- Thermal limiting built into the Jazz drive itself — no special HMI configuration needed
- Memory: automatically resumes the last speed and brightness settings on power-up

## What Makes It Different
- **vs. SmartAIR / TouchAIR:** Jazz HMI is a Jazz-only device. It can't control Sailfin fans. Conversely, SmartAIR and TouchAIR can't directly control Jazz fans — TouchAIR can supervise a Jazz network as a separate zone, but uses the Jazz HMI's network underneath.
- **vs. Jazz Multi-Fan HMI:** the single-fan Jazz HMI handles 1 fan. The multi-fan version looks identical but controls up to 5 Jazz fans daisy-chained with CAT-5.

## Power & Electrical Requirements
- Draws power from the Jazz Fan via the CAT-5 / communication cable (the Jazz Fan has on-board controls and supplies the HMI)
- No separate power supply needed
- Max permissible control cable length (from Jazz spec sheet): 30 metres unshielded — this is the overall Jazz control cable limit

## Mounting & Installation Notes
- Mount in a safe, dry, indoor location — the Jazz Fan itself is rated IP54 / NEMA 3 for indoor use only; the HMI follows the same rule
- Connect the 100 ft CAT-5 between the Jazz Fan's motor assembly and the HMI per the installation guide
- Do NOT run the control cable in the same conduit as the Jazz power cable
- Only qualified electricians should install the drive and motor connections

## Maintenance Requirements
- Jazz fans have automatic thermal limiting — no operator action needed
- No routine HMI maintenance documented
- Do not work on the drive, motor cable, or motor when input power is applied
- After disconnecting input power, wait 5 minutes for capacitors to discharge before working on the drive

## Compatible Accessories & Controls
- **Jazz Fan** — required
- **Jazz Multi-Fan HMI** — the multi-fan upgrade (replaces single-fan HMI with a multi-fan one)
- **TouchAIR** — can supervise a Jazz network as a separate zone

## Common FAQs

**Q: Do I have to buy the Jazz HMI separately?**
A: No. It is included with every Jazz Fan.

**Q: How long is the communication cable?**
A: 100 ft CAT-5, included. The overall Jazz control cable length limit is 30 metres unshielded per the Jazz installation guide.

**Q: Can the Jazz HMI control multiple fans?**
A: Not the single-fan HMI. For up to 5 Jazz fans, use the Jazz Multi-Fan HMI.

**Q: Can I use the Jazz HMI to control a Sailfin fan?**
A: No. Jazz fans and Altra-Air Sailfin fans are on different networks and different HMIs. Jazz HMI only controls Jazz.

**Q: Can SmartAIR or TouchAIR control my Jazz fan?**
A: SmartAIR cannot. TouchAIR can supervise a Jazz network as a separate zone. Jazz always has its own HMI network underneath.

**Q: Does the Jazz HMI dim the LED?**
A: Yes — the Jazz Fan's integrated 1,980-lumen LED is dimmable from the HMI.

**Q: Is the Jazz HMI outdoor rated?**
A: No. The Jazz Fan system is rated IP54 / NEMA 3 and is for indoor use only.

## Source Documents Referenced
- `EN561X8455 Jazz_Installation Guide_EN__Rev-03__05.29.2025 (pdfplumber).txt`
- `JazzDesign&EngineeringGuide-Updated10.18.2024 (pdfplumber).txt`
- `JazzBrochure_2019Mockup (pdfplumber).txt`
- `Control Options (2023)__Brochure_EN__Rev-01__03.04.2023 (pdfplumber).txt`
