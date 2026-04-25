---
id: lvc-vs-smartair
name: LVC (+ TFD-1) vs. SmartAIR
type: comparison
compares: [lvc, tfd-1, smartair, smartair-multifan]
source_docs:
  - "Control Options (2023)__Brochure_EN__Rev-01__03.04.2023 (pdfplumber).txt"
  - "Electrical Installation Guide 2022 (pdfplumber).txt"
  - "Electrical Installation Guide - Schneider Drive - 2023-09142023- FullDocument-Version8 (pdfplumber).txt"
last_verified: 2026-04-11
---

# LVC (+ TFD-1) vs. SmartAIR

## TL;DR
- **LVC + TFD-1** — analogue 0–10 V zone control with dial-based temperature automation. Lenze VFD path. Budget, no touchscreen, temperature only.
- **SmartAIR** — digital touchscreen HMI with temperature **and humidity** automation, LED dimming, real-time drive data. Schneider VFD path.

Both are valid automation options. The right choice depends on budget, whether humidity matters, and which VFD is already specified.

## When to choose LVC + TFD-1
- Facility is already on the Lenze VFD path (ZoneAIR)
- Operators prefer physical dials to touchscreens
- Temperature automation is enough — no humidity requirement
- Budget is the primary driver

## When to choose SmartAIR
- Need humidity automation (dairy, hog, poultry — anywhere humidity matters as much as heat)
- Want LED dimming from the HMI
- Want real-time drive data on a screen (status, alarms, fault history)
- Already on the Schneider VFD path

## Side-by-side
| Item | LVC + TFD-1 | SmartAIR |
|---|---|---|
| VFD path | Lenze AC Tech | Schneider |
| Interface | Dial + panel | Touchscreen |
| Temperature auto | **Yes** (set point + modulation band + min vent off) | **Yes** |
| Humidity auto | **No** | **Yes** |
| LED dimming | No (LED controlled separately) | **Yes** |
| Wind sensor | Yes (analogue input) | Yes (control box input) |
| Fire relay | Yes | Yes |
| Real-time drive data display | No | Yes |
| Max fans | 7 (ZoneAIR) / 10 (LVC → Schneider 6-wire) | 1 / 10 (multi-fan) |
| Min speed | 15 Hz / 27 % | 15 Hz / 27 % |
| Alarm display | No | Yes (on HMI) |

## Feature depth

### Temperature automation
Both achieve the same outcome: fan speed ramps from minimum to 100 % as temperature rises through a configured band.

- **TFD-1:** three physical dials — set point, modulation band, min vent off. Example: 20 °C set point, 10 °C band, 5 °C off → fan runs 27 % at 20 °C, 100 % at 30 °C, stops below 15 °C.
- **SmartAIR:** set via the touchscreen. Values are stored digitally. Multi-fan caveat: auto-mode settings are NOT retentive on power loss and must be re-enabled manually.

### Humidity (SmartAIR only)
SmartAIR can also run the fans based on humidity — critical in dairy, hog, and poultry facilities where latent heat from moisture matters as much as dry-bulb temperature. TFD-1 cannot do this.

### LED control (SmartAIR only)
SmartAIR dims and switches the integrated LED light on each Sailfin. On the LVC + TFD-1 path, LED is controlled separately.

### Diagnostics
SmartAIR shows drive status, current, frequency, and fault codes in real time. TFD-1 has no display — the operator sees dial positions only.

## Cost and complexity (qualitative)
- LVC + TFD-1: lowest cost for temperature automation on 2–7 fans
- SmartAIR single-fan: moderate cost, full feature set on one fan
- SmartAIR Multi-Fan: highest cost of these options but supports up to 10 fans with full features

## Common FAQs

**Q: Can I get humidity automation on the Lenze / LVC path?**
A: No. Humidity automation is SmartAIR-only.

**Q: Can TFD-1 drive a SmartAIR system?**
A: No. TFD-1 is specifically an LVC add-on and speaks 0–10 V. SmartAIR runs its own digital auto-mode logic.

**Q: If I already have SmartAIR, do I need TFD-1?**
A: No. SmartAIR already has built-in temperature (and humidity) automation.

**Q: Can I use SmartAIR just for the display but let TFD-1 control the fans?**
A: No. They are two separate control paths (Schneider vs. Lenze). Pick one.

**Q: Is SmartAIR "better"?**
A: In features, yes — humidity, LED, diagnostics. In cost, no — LVC + TFD-1 is cheaper for facilities that only need temperature automation.

## Source Documents Referenced
- `Control Options (2023)__Brochure_EN__Rev-01__03.04.2023 (pdfplumber).txt`
- `Electrical Installation Guide 2022 (pdfplumber).txt`
- `Electrical Installation Guide - Schneider Drive - 2023-09142023- FullDocument-Version8 (pdfplumber).txt`
