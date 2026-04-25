---
id: warranty
name: Warranty Overview
type: guide
category: warranty
applies_to: [sailfin-geared, sailfin-gearless, jazz-fan, aisle-air, alite-3]
source_docs:
  - "Envira-North 2025__Catalogue__EN__Rev-03__11.27.2025 (pdfplumber).txt"
  - "Altra-AirSailfin_Design&Engineering_2022 (pdfplumber).txt"
  - "Altra-AirSailfinGearless_Design&Engineering_202215YearWarranty (pdfplumber).txt"
  - "EN921X8240 Altra-AirSailfin_Geared&Gearless_InstallationGuide_11142024 (pdfplumber).txt"
last_verified: 2026-04-11
---

# Warranty Overview

## Overview
Envira-North provides a manufacturer's warranty on HVLS fans, drives, and controls. Specific warranty terms and duration are product- and region-dependent and are published in the current catalogue and on the Envira-North website. This page summarises the behaviours that void warranty and the actions required to preserve warranty coverage — for the exact terms on a given SKU, contact Envira-North Customer Support.

## Actions that void warranty

### Motor / drive
- **Running below 15 Hz / 27 % minimum fan speed** — this is the most common warranty-voiding mistake. Below this speed the motor does not move enough air to cool itself and overheats. The limit is hard-coded in the factory configuration — do NOT lower it.
- **Exceeding cable-length limits on a Lenze drive** without a load reactor or dV/dT filter — reflected-wave overvoltage damages motor windings
- **Using a non-Envira-North VFD** — the drive is matched to the motor at the factory
- **Operating a geared Sailfin with the rubber vent plug still installed** on first start-up — pressure builds in the gearbox and blows a seal
- **Skipping the 20,000-hour gearbox oil change** on a geared Sailfin

### Installation
- **Skipping the wind sensor on an agricultural installation** — mandatory
- **Removing a factory jumper** (wind sensor, fire relay) without installing the real device — the fan will not operate anyway
- **Mounting without a structural review** — the dynamic load must be verified
- **Installing indoor-rated fans (Jazz, Alite) in wet / outdoor locations**

### Electrical
- **Unbonded fan structure** — safety and electrical compliance
- **Shared conduit with motor power and 0–10 V LVC signal** — signal corruption and noise faults are not covered
- **Using the external RJ45 on a Schneider drive** — all connections must be inside an enclosure

### Maintenance
- **Skipping the 6-month initial inspection**
- **Skipping 18-month periodic inspections**
- **Working on a Jazz drive without waiting 5 minutes for capacitor discharge** — safety issue, also a warranty concern if damage results

## Actions that preserve warranty
- Install per the Envira-North installation guide for the product
- Use only Envira-North drives and controls matched to the fan
- Follow the maintenance schedule in `guides/maintenance-schedule.md`
- Keep a log of inspections, oil changes, and any service actions
- Contact Envira-North Customer Support before making any non-standard modification

## Claiming a warranty issue
1. Gather the product SKU, serial number, and install date
2. Gather maintenance records
3. Describe the symptom, when it started, and any error codes displayed on the HMI
4. Contact Envira-North Customer Support — they will triage and authorise return / replacement / on-site service

## Altra-Air Sailfin warranty terms (from D&E and installation guides)

### Standard Three-Year Limited Warranty — coverage by component
| Component | Coverage |
|---|---|
| Air Foil Shaped Blade | **Lifetime Warranty** |
| Aluminum Alloy Hub | **Lifetime Warranty** |
| Mounting System (blades, hub & frame) | **Lifetime Warranty** |
| Motor / Gear Motor | 3-Year Limited Warranty |
| Gear Reducer (geared only) | 3-Year Limited Warranty |
| VFD Control Panel | 3-Year Limited Warranty |
| Labour (pre-approved) | 1-Year Limited Warranty |
| Custom Fan Wraps / Paint | 1-Year Limited Warranty |

**Labour warranty note:** Labour Warranty covers all reasonable costs paid by the customer to an independent contractor (including dealers) to remove, dismantle, reassemble, or reinstall any warranted product during the first year. Labour estimate must be **pre-approved by Envira-North** before proceeding. All receipts are submitted to Envira-North and are paid upon completion and after return of the failed unit. Envira-North will only issue a credit/cheque to the customer/dealer, not pay the contractor directly.

**Replacement part coverage:** Parts replaced or repaired under warranty are warranted for **90 days** from shipment date of the replacement, or the remainder of the original warranty period, whichever is longer.

### Fifteen-Year Service Life Prorated Warranty

**Scope:** Applies only to the original End-User; cannot be transferred. Applies to U.S. and Canada purchases only. Outside U.S. and Canada, the standard Three-Year Warranty applies.

**What it covers:** In addition to the Lifetime Warranty on blades, hub, and frame, and the standard Three-Year Limited Warranty on all other components, the Warrantor warrants that the product will have a **service life of Fifteen Years from the date of purchase** when used in accordance with the operation and maintenance procedures prescribed in the Envira-North Systems' Installation Manuals.

**Prorated credit formula:**
- **Year 1–3:** Product repaired or replaced pursuant to the terms of the Three-Year Limited Warranty
- **Year 4–15:** Unit Credit ($) = Current List Price × (Years of Unexpired Life / 15 Years of Warranted Life)

**Registration requirement:** The warranty is **NOT VALID** unless:
- (a) The End-User returns to Company the **Warranty Registration Card within thirty (30) days of purchase**; AND
- (b) The product's serial numbers have not been removed or are not illegible; AND
- (c) Maintenance records are submitted at time of performing the Recommended Maintenance Schedule, **minimum every 18 months**

**Registration method:** Complete the Fifteen Year Service Life Prorated Warranty Form and return within 30 days of purchase by fax to 1(519)527-2560 OR email bigair@enviranorth.com.

**What the 15-Year Warranty does NOT cover:**
- Defects or damages caused by: failure to properly store before installation; shipping/delivery if FOB Factory; neglect, accident, abuse, misuse, misapplication, or incorrect installation; repair or alteration not authorized in writing; improper testing, operation, maintenance, or modification not authorized in writing; use under other than normal operating conditions
- Controls and any other external electronic controlling devices
- Exclusions listed in the standard Three-Year Limited Warranty
- Any products or components purchased prior to the effective date of this warranty

**End-User obligations for 15-Year Warranty:**
- Use the product in a normal way
- Follow the product's Installation Manuals
- Protect against further damage if there is a covered defect
- **Submit maintenance records at time of performing the Recommended Maintenance Schedule, minimum every 18 months**

### Warranty claim procedure (step-by-step)
1. Contact your original dealer/salesman when you first notice a problem
2. The dealer/salesman assists in determining which product is causing the problem
3. If they cannot diagnose it, contact Envira-North with all necessary information
4. The appropriate Envira-North department will contact the customer to determine the cause
5. Once diagnosed, submit a Purchase Order for a replacement component complete with price
6. Replacement component will be shipped out upon receipt of the PO
7. Once units have been changed over, submit all pre-approved costs to Envira-North for payment
8. No credits or cheques will be issued until all original products are received back at Envira-North (or unless Envira-North directs otherwise)

**To obtain warranty service:** Call Envira-North Systems Ltd. Service at **1-866-771-7766** or **1-519-527-2198**. Products must be returned with a proper Return Authorization Number attached, delivered FOB Company factory.

## For specific warranty duration and terms
See the component table above for Altra-Air Sailfin warranty durations. **Contact Envira-North Customer Support** for the specific warranty term on other products and regions.

## Common pitfalls
- Operators unaware of the 15 Hz / 27 % minimum — then lowering speed further "to save power"
- Electricians routing LVC signal in the same conduit as motor power
- Agricultural installs without a wind sensor
- Missing the geared-Sailfin vent plug step
- Forgetting to log maintenance — making a future warranty claim harder

## Source Documents Referenced
- `Envira-North 2025__Catalogue__EN__Rev-03__11.27.2025 (pdfplumber).txt`
- `Altra-AirSailfin_Design&Engineering_2022 (pdfplumber).txt`
- `Altra-AirSailfinGearless_Design&Engineering_202215YearWarranty (pdfplumber).txt`
- `EN921X8240 Altra-AirSailfin_Geared&Gearless_InstallationGuide_11142024 (pdfplumber).txt`
