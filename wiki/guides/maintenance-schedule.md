---
id: maintenance-schedule
name: Maintenance Schedule — All Products
type: guide
category: maintenance
applies_to: [sailfin-geared, sailfin-gearless, jazz-fan, aisle-air, alite-3]
source_docs:
  - "Envira-North 2025__Catalogue__EN__Rev-03__11.27.2025 (pdfplumber).txt"
  - "Control Options (2023)__Brochure_EN__Rev-01__03.04.2023 (pdfplumber).txt"
  - "Altra-AirSailfin_Design&Engineering_2022 (pdfplumber).txt"
  - "Altra-AirSailfinGearless_Design&Engineering_202215YearWarranty (pdfplumber).txt"
  - "EN921X8240 Altra-AirSailfin_Geared&Gearless_InstallationGuide_11142024 (pdfplumber).txt"
last_verified: 2026-04-11
---

# Maintenance Schedule — All Products

## Overview
Envira-North fans follow a two-phase maintenance schedule: an initial inspection at 6 months, then a regular inspection every 18 months. Geared Sailfin has additional gearbox-specific requirements. Jazz has drive-capacitor safety rules. This guide consolidates the schedule for all products.

## Mandatory safety rules before any maintenance
The following safety rules apply to **all** maintenance on Altra-Air Sailfin fans (from the official maintenance schedule):
1. No maintenance shall be done on the fan, mount, or guy wires while it is in operation or powered.
2. No maintenance shall be done on the fan controller while powered unless the task involves reprogramming or troubleshooting the electrical system.
3. No maintenance shall be done within a **6 m horizontal radius** of the fan and **4 ft below** — and none above — the blade level while it is in operation.
4. While doing maintenance, a **safety barrier shall be erected at a radius of 6 m** of the centre of the fan.
5. The fan controller shall be **locked out** while maintenance is ongoing on the fan, mount, or guy wires.
6. All personnel shall wear appropriate **personal safety equipment** as mandated by local, provincial, and national regulations.
7. A **risk assessment** shall be performed before any maintenance.
8. A **tailboard meeting** shall be performed before any work is done, including a checklist with emergency contacts for the area.

> **Note:** The maintenance schedule is based on running **5,000 hours / year** and is a guideline to ensure safe and continuous operation. In cases of extreme operating conditions (high humidity, aggressive environments, large temperature variations), **shorter intervals** between service are recommended.

## Sailfin — Gearless
| Interval | Task |
|---|---|
| 6 months (initial) | Visual inspection: blade hardware torque, hub bolts, safety cable, mounting kit hardware, VFD enclosure seals |
| Every 18 months | Full inspection: torque check, wobble test, clean blades, clean VFD enclosure, verify HMI comms, wind-sensor function test (if installed) |
| As needed | Blade replacement if damaged — do not run a fan with a bent / chipped blade |

- Gearless = direct-drive, no gearbox, no oil change
- HMI / control side: no routine maintenance documented

### Gearless — Blades
Blades are extruded from **6063-aluminum alloy, heat-treated to T-5 condition**, anodized to 0.0004" (10 Microns) clear for corrosion resistance and ease of cleaning. They carry a **lifetime warranty**.

| Interval | Task |
|---|---|
| Initial 6 months | Ensure blades are intact, level, and clean as required |
| Every 18–36 months thereafter | Full blade inspection |

### Gearless — Drop / Mounting
| Interval | Task |
|---|---|
| Initial 6 months | Physical check of fan guy wires, re-tightening of clamps if required |
| Initial 6 months | Check all nuts/bolts/clamps (missing/loose/damaged) |
| Initial 6 months | Physical check of safety cable, re-tightening of clamps if required |
| Every 18 months thereafter | Repeat above |

### Gearless — Control Panel (VFD)
Controls are variable frequency drives providing soft start/stop, variable speed control, and overload protection. They carry a **3-year limited warranty**.

| Interval | Task |
|---|---|
| Initial 12 months | Check for loose/discoloured wires |
| Initial 12 months | Check for hot spots |
| Initial 12 months | Re-tighten all loose electrical connections |
| Every 18 months thereafter | Repeat above |

## Sailfin — Geared
| Interval | Task |
|---|---|
| Before first start-up | **Remove the rubber vent plug** from the gearbox (discard after removal) |
| Before first start-up | Discard pink tag if attached to unit |
| 6 months (initial) | Visual inspection (same as gearless) + gearbox oil level check |
| 18 months (initial) | **Check oil level** on gear reducer |
| 20,000 operating hours | **Full oil change** (Nord Helical Gear Reducer) |
| Every 18 months | Full inspection (same as gearless) |

- Use the oil grade specified in the Nord gearmotor manual
- Do not mix oil grades

### Geared — Motor (Power Unit)
Motors are wound with **200°C moisture resistant Inverter Spike Resistant (ISR) magnetic wire**, which dramatically extends motor life compared to motors with non-ISR wire. They carry a **3-year limited warranty**.

| Interval | Task |
|---|---|
| Initial 6 months | Check for hot spots |
| Initial 6 months | Re-tighten all loose electrical connections |
| Every 18 months thereafter | Repeat above |

### Geared — Gear Reducer / Motor (Nord Helical Gear Reducer)
The Altra-Air Geared fan is driven through **Nord Helical Gear Reducers/Gearmotors**. They carry a **3-year limited warranty**.

| Interval | Task |
|---|---|
| Initial 18 months | Check oil level |
| Every 20,000 hours of normal use | **Change oil** |

### Geared — Blades
Blades (installation guide spec): extruded from **6005-aluminum alloy, heat-treated to T-61 condition**, anodized to 10 Microns (0.0004") clear. They carry a **lifetime warranty**.

| Interval | Task |
|---|---|
| Initial 6 months | Ensure blades are intact, level, and clean as required |
| Every 18–36 months thereafter | Full blade inspection |

### Geared — Drop / Mounting
(Same schedule as Gearless — see above)

### Geared — Control Panel (VFD)
(Same schedule as Gearless — see above)

## Jazz
- **Automatic thermal limiting** — the Jazz drive handles it, no operator action
- No routine HMI maintenance documented
- **Safety rule:** after disconnecting input power, wait **5 minutes** for drive capacitors to discharge before touching the drive, motor cable, or motor
- Inspect the integrated LED module at the 18-month interval; replace with the EN561X3675 LED kit if failed

## Aisle-Air
- IP55 housing — wipe down housing at routine intervals
- Check Modbus communication status on the host controller
- Inspect the 15 MPH discharge for obstructions

## Alite 3
- Routine maintenance not fully documented in the source (OCR gap)
- Contact Envira-North Customer Support for the specific schedule
- General rule: visual inspection at 6 months, then every 18 months

## Hurricane (passive turbine)
- No moving drive — the turbine spins on bearings driven by wind and thermal buoyancy
- Inspect bearings and Vari-Pitch flue at a 12-month interval (suggested)
- Clean debris out of the throat annually

## Controls and accessories
- **Wind sensor:** inspect cup / vane for damage and free rotation; verify trigger before each heavy-use season
- **Fire relay:** test with the building's fire panel per the facility's fire-system maintenance schedule
- **VFDs:** clean enclosure vents, verify no moisture ingress, check fan (if internal) at the 18-month interval
- **HMIs:** no routine maintenance

## Lock-out / tag-out for all maintenance
1. Switch off the fan at the HMI / keypad
2. Open the local disconnect and lock it
3. Verify zero voltage at the drive input
4. Wait 5 minutes (Jazz) for capacitor discharge
5. Proceed with the physical task
6. Re-energise, verify operation, record the work in the facility log

## Record-keeping
- Log every inspection and every oil change
- Record commissioning date, 6-month inspection date, each 18-month inspection date, and each gearbox oil change
- Keep records for the warranty period (see `guides/warranty.md`)

## Common pitfalls
- Skipping the gearbox vent plug removal on first start-up → blown seal
- Running below 15 Hz / 27 % → motor overheats, warranty voided
- Working on a Jazz drive before the 5-minute capacitor discharge → shock hazard
- Forgetting the wind sensor seasonal test on agricultural installs

## Source Documents Referenced
- `Envira-North 2025__Catalogue__EN__Rev-03__11.27.2025 (pdfplumber).txt`
- `Control Options (2023)__Brochure_EN__Rev-01__03.04.2023 (pdfplumber).txt`
- `Altra-AirSailfin_Design&Engineering_2022 (pdfplumber).txt`
- `Altra-AirSailfinGearless_Design&Engineering_202215YearWarranty (pdfplumber).txt`
- `EN921X8240 Altra-AirSailfin_Geared&Gearless_InstallationGuide_11142024 (pdfplumber).txt`
