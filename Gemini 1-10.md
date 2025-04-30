Okay, here are the step-by-step solutions to the physics problems presented in the images.

**Navigation**

*   [Opgave 1: Proptrækker (Corkscrew)](#opgave-1-proptrækker-corkscrew)
*   [Opgave 2: PET-skanning (PET Scan)](#opgave-2-pet-skanning-pet-scan)
*   [Opgave 3: Skærmfilter (Screen Filter)](#opgave-3-skærmfilter-screen-filter)
*   [Opgave 4: NTC resistor](#opgave-4-ntc-resistor)
*   [Opgave 5: E-cigaret (E-cigarette)](#opgave-5-e-cigaret-e-cigarette)
*   [Opgave 6: Alcator C-Mod (Tokamak)](#opgave-6-alcator-c-mod-tokamak)
*   [Opgave 7: Curiosity (Mars Lander)](#opgave-7-curiosity-mars-lander)
*   [Opgave 8: Hot Stone massage](#opgave-8-hot-stone-massage)
*   [Opgave 9: Antennagalaksen (Antennae Galaxies)](#opgave-9-antennagalaksen-antennae-galaxies)
*   [Opgave 10: Meget lille pacemaker (Tiny Pacemaker)](#opgave-10-meget-lille-pacemaker-tiny-pacemaker)

---

## Opgave 1: Proptrækker (Corkscrew)

![Opgave 1 Image 1](images/image_0.png)
![Opgave 1 Image 2](images/image_1.png)

**a) Beregn vinens densitet.**

*   **Goal:** Calculate the density (massefylde, ρ) of the wine.
*   **Knowns:**
    *   Volume, V = 0.75 L
    *   Mass, m = 0.73 kg
*   **Formula:** Density is defined as mass per unit volume:
    ```
    ρ = m / V
    ```
*   **Unit Conversion:** To get the density in standard SI units (kg/m³), we need to convert the volume from liters (L) to cubic meters (m³). We know that 1 L = 0.001 m³.
    ```
    V = 0.75 L * (0.001 m³ / 1 L) = 0.00075 m³
    ```
*   **Calculation:** Substitute the mass and converted volume into the density formula:
    ```
    ρ = 0.73 kg / 0.00075 m³
    ρ ≈ 973.33 kg/m³
    ```
*   **Significant Figures:** Both mass and volume are given with two significant figures. Therefore, the result should also be rounded to two significant figures.
    ```
    ρ ≈ 970 kg/m³
    ```
*   **Answer:** Vinens densitet er ca. **970 kg/m³**.

**b) Vurdér størrelsen af den gennemsnitlige effekt, hvormed kraften F udfører arbejde på proppen under åbningen af vinen. Bilag 1 kan benyttes ved besvarelsen.**

*   **Goal:** Estimate the average power (gennemsnitlig effekt, P_avg) exerted by force F during the opening process.
*   **Knowns:**
    *   Graph of Force (F) vs. Displacement (s).
    *   Duration of opening, Δt = 2.3 s.
*   **Formula:**
    *   Average power is the total work done (Arbejde, W) divided by the time taken (Δt):
        ```
        P_avg = W / Δt
        ```
    *   Work done by a variable force is the area under the Force-Displacement (F-s) graph:
        ```
        W = ∫ F ds ≈ Area under F-s curve
        ```
*   **Step 1: Estimate Work (Area under the graph)**
    We need to estimate the area under the curve in the F/N vs s/m graph. The force acts from s=0 until the cork is out. From the graph, the force seems to become negligible around s ≈ 0.038 m. We can approximate the area by dividing it into geometric shapes or by counting squares. Let's approximate using a triangle and a trapezoid:
    *   **Region 1 (Triangle approx.):** From s=0 to s=0.015 m. The peak force is about 320 N.
        ```
        Area₁ ≈ (1/2) * base * height ≈ 0.5 * (0.015 m) * (320 N) = 2.4 J
        ```
    *   **Region 2 (Trapezoid approx.):** From s=0.015 m to s=0.038 m. The force decreases from 320 N to roughly 0 N (let's say ~20 N at s=0.035, near zero at 0.038). Let's take the end point for the area calculation where significant force is applied, maybe s = 0.035 m where F ≈ 50 N.
        ```
        Area₂ ≈ (1/2) * (height₁ + height₂) * width ≈ 0.5 * (320 N + 50 N) * (0.035 m - 0.015 m)
        Area₂ ≈ 0.5 * (370 N) * (0.020 m) = 3.7 J
        ```
    *   **Total Work (Estimate):**
        ```
        W ≈ Area₁ + Area₂ ≈ 2.4 J + 3.7 J = 6.1 J
        ```
    *(Note: This is an estimation. Counting squares might yield a slightly different result, but this method gives a reasonable approximation.)*
*   **Step 2: Calculate Average Power**
    Now use the estimated work and the given time:
    ```
    P_avg = W / Δt ≈ 6.1 J / 2.3 s
    P_avg ≈ 2.65 W
    ```
*   **Significant Figures:** The time is given with 2 significant figures, and our work estimate is approximate. Rounding to two significant figures seems appropriate.
    ```
    P_avg ≈ 2.7 W
    ```
*   **Answer:** Størrelsen af den gennemsnitlige effekt er vurderet til ca. **2.7 W**.

---

## Opgave 2: PET-skanning (PET Scan)

![Opgave 2 Image](images/image_2.png)

**a) Opskriv kernereaktionen, hvor beskydningen af ¹⁶O med protoner giver ¹³N og en anden kerne. Begrund, hvilken anden kerne der dannes.**

*   **Goal:** Write the nuclear reaction equation and identify the unknown product nucleus.
*   **Reaction Scheme:** ¹⁶O + p → ¹³N + ?
*   **Principles:** In any nuclear reaction, the total nucleon number (A, mass number) and the total proton number (Z, atomic number) must be conserved.
*   **Identify Reactants:**
    *   Oxygen-16 (¹⁶O): Z = 8, A = 16
    *   Proton (p or ¹H): Z = 1, A = 1
*   **Identify Known Product:**
    *   Nitrogen-13 (¹³N): Z = 7, A = 13
*   **Let the unknown product be denoted by AZX.**
*   **Conservation of Nucleon Number (A):**
    ```
    A_reactants = A_products
    16 + 1 = 13 + A_X
    17 = 13 + A_X
    A_X = 17 - 13 = 4
    ```
*   **Conservation of Proton Number (Z):**
    ```
    Z_reactants = Z_products
    8 + 1 = 7 + Z_X
    9 = 7 + Z_X
    Z_X = 9 - 7 = 2
    ```
*   **Identify Unknown Product (X):** The nucleus with A = 4 and Z = 2 is Helium-4 (⁴He), also known as an alpha particle (α).
*   **Reaction Equation:**
    ```
    ¹⁶O + ¹p → ¹³N + ⁴He
    ```
    or
    ```
    ¹⁶₈O + ¹₁p → ¹³₇N + ⁴₂He
    ```
*   **Begrundelse (Justification):** Kernen ⁴He (en alpha-partikel) dannes, fordi både nukleontallet (A) og protontallet (Z) skal bevares i kernereaktionen. Summen af A på venstre side (16+1=17) skal være lig summen af A på højre side (13+4=17). Ligeledes skal summen af Z på venstre side (8+1=9) være lig summen af Z på højre side (7+2=9).

**b) Hvor stor var aktiviteten af ¹³N, da prøven blev fremstillet i acceleratoren?**

*   **Goal:** Calculate the initial activity (A₀) of the ¹³N sample when it was produced.
*   **Knowns:**
    *   Activity upon arrival (A(t)) = 575 MBq (Mega-Becquerel)
    *   Transport time (t) = 15 minutter
    *   Half-life of ¹³N (T½) - *This must be looked up.* T½(¹³N) ≈ 9.97 minutter.
*   **Formula:** Radioactive decay law relates activity at time t (A(t)) to the initial activity (A₀) and the decay constant (λ):
    ```
    A(t) = A₀ * e^(-λt)
    ```
    The decay constant is related to the half-life:
    ```
    λ = ln(2) / T½
    ```
*   **Derivation:** We need to find A₀:
    ```
    A₀ = A(t) / e^(-λt) = A(t) * e^(λt)
    A₀ = A(t) * e^((ln(2)/T½) * t)
    ```
*   **Calculation:** Ensure units for t and T½ are consistent (both in minutes).
    ```
    λ = ln(2) / 9.97 min ≈ 0.06952 min⁻¹
    A₀ = 575 MBq * e^(0.06952 min⁻¹ * 15 min)
    A₀ = 575 MBq * e^(1.0428)
    A₀ ≈ 575 MBq * 2.837
    A₀ ≈ 1631.3 MBq
    ```
*   **Significant Figures:** The given activity (575 MBq) and time (15 min) have 3 and 2 significant figures respectively. The half-life has 3. Let's round to two significant figures based on the transport time.
    ```
    A₀ ≈ 1600 MBq
    ```
    or in Giga-Becquerel (GBq):
    ```
    A₀ ≈ 1.6 GBq
    ```
*   **Answer:** Aktiviteten af ¹³N, da prøven blev fremstillet, var ca. **1.6 GBq** (eller 1600 MBq).

**c) Vurdér, hvor meget energi der afsættes i patienten fra henfald af ¹³N i den første halve time efter indsprøjtningen af ¹³N.**

*   **Goal:** Estimate the total energy deposited in the patient during the first 30 minutes after injection.
*   **Knowns:**
    *   Initial activity injected into patient (A₀_pat). We assume this is the activity upon arrival: A₀_pat = 575 MBq = 575 * 10⁶ Bq (decays/second).
    *   Energy deposited per decay (E_decay) = 189 fJ = 189 * 10⁻¹⁵ J. *(Interpretation: The text "Ved hvert henfald...afsættes energien 189 fJ" implies this is energy per decay.)*
    *   Time interval (Δt) = 30 minutter.
    *   Half-life (T½) = 9.97 minutter.
    *   Decay constant (λ) ≈ 0.06952 min⁻¹ (from part b).
*   **Method:**
    1.  Calculate the number of decays (N_decay) that occur within the 30-minute interval.
    2.  Calculate the total energy deposited (E_total) by multiplying the number of decays by the energy per decay.
*   **Formula:**
    *   The number of radioactive nuclei remaining at time t is N(t) = N₀ * e^(-λt).
    *   The initial number of nuclei is N₀ = A₀ / λ.
    *   The number of decays in the interval from 0 to t is N_decay(t) = N₀ - N(t) = N₀ * (1 - e^(-λt)).
    *   Total Energy E_total = N_decay * E_decay.
*   **Calculation:**
    *   Convert time units to be consistent. Let's use minutes.
        *   A₀_pat = 575 * 10⁶ decays/s * (60 s/min) = 3.45 * 10¹⁰ decays/min.
        *   λ ≈ 0.06952 min⁻¹.
        *   t = 30 min.
    *   Calculate initial number of nuclei N₀:
        ```
        N₀ = A₀_pat / λ = (3.45 * 10¹⁰ min⁻¹) / (0.06952 min⁻¹) ≈ 4.962 * 10¹¹ nuclei
        ```
    *   Calculate the number of decays in 30 minutes:
        ```
        N_decay(30 min) = N₀ * (1 - e^(-λ * 30))
        N_decay(30 min) ≈ (4.962 * 10¹¹) * (1 - e^(-0.06952 * 30))
        N_decay(30 min) ≈ (4.962 * 10¹¹) * (1 - e^(-2.0856))
        N_decay(30 min) ≈ (4.962 * 10¹¹) * (1 - 0.1242)
        N_decay(30 min) ≈ (4.962 * 10¹¹) * 0.8758 ≈ 4.346 * 10¹¹ decays
        ```
    *   Calculate the total energy deposited:
        ```
        E_total = N_decay(30 min) * E_decay
        E_total ≈ (4.346 * 10¹¹ decays) * (189 * 10⁻¹⁵ J/decay)
        E_total ≈ 8.214 * 10⁻² J
        ```
*   **Significant Figures:** A₀_pat has 3 sig figs, E_decay has 3, t has 1 (or maybe 2 if "halve time" implies 30.0). T½ has 3. Let's use 3 significant figures.
    ```
    E_total ≈ 8.21 * 10⁻² J
    ```
    This can also be written as 82.1 mJ (milliJoules).
*   **Answer:** Der afsættes ca. **8.21 x 10⁻² J** (eller 82.1 mJ) energi i patienten i løbet af den første halve time.

---

## Opgave 3: Skærmfilter (Screen Filter)

![Opgave 3 Image 1](images/image_3.png)
![Opgave 3 Image 2](images/image_4.png)

**a) Brug billedet til at bestemme afstanden mellem spalterne i skærmfilteret.**

*   **Goal:** Determine the slit separation (d) of the screen filter (acting as a diffraction grating).
*   **Knowns:**
    *   Distance from filter to wall (screen), L = 1.20 m.
    *   Wavelength of laser light, λ = 632 nm = 632 * 10⁻⁹ m.
    *   Image shows the diffraction pattern on a ruler.
    *   The 0th order maximum (n=0) is at the 10.0 cm mark on the ruler.
*   **Image Analysis:** We need to find the position of a higher-order maximum (e.g., n=1) relative to the central maximum.
    *   Central maximum (n=0) position: x₀ = 10.0 cm.
    *   First-order maximum (n=1) positions appear to be at approximately 7.5 cm and 12.5 cm.
    *   The distance from the center to the first-order maximum (x₁) is:
        ```
        x₁ = |12.5 cm - 10.0 cm| = 2.5 cm
        ```
        or
        ```
        x₁ = |7.5 cm - 10.0 cm| = 2.5 cm
        ```
    *   So, x₁ = 2.5 cm = 0.025 m.
*   **Formula:** The condition for constructive interference (bright fringes/maxima) for a diffraction grating is:
    ```
    d * sin(θn) = n * λ
    ```
    where d is the slit separation, θn is the angle to the nth order maximum, n is the order number (n=0, 1, 2,...), and λ is the wavelength.
    The angle θn can be related to the position xn on the screen and the distance L using trigonometry:
    ```
    tan(θn) = xn / L
    ```
    For small angles, sin(θn) ≈ tan(θn) ≈ xn / L. Let's check if the angle is small:
    ```
    θ₁ = arctan(x₁ / L) = arctan(0.025 m / 1.20 m) ≈ arctan(0.0208) ≈ 1.19°
    ```
    Since the angle is very small (< 5°), the small angle approximation is valid.
*   **Derivation using approximation:**
    ```
    d * (xn / L) ≈ n * λ
    d ≈ (n * λ * L) / xn
    ```
*   **Calculation:** Using the first-order maximum (n=1):
    ```
    d ≈ (1 * (632 * 10⁻⁹ m) * 1.20 m) / (0.025 m)
    d ≈ (7.584 * 10⁻⁷ m²) / (0.025 m)
    d ≈ 3.0336 * 10⁻⁵ m
    ```
*   **Significant Figures:** L has 3 sig figs, λ has 3 sig figs, x₁ (read from ruler) likely has 2 sig figs (2.5 cm). The result should be rounded to 2 significant figures.
    ```
    d ≈ 3.0 * 10⁻⁵ m
    ```
    This can also be expressed as 30 μm (micrometers).
*   **Answer:** Afstanden mellem spalterne i skærmfilteret er ca. **3.0 x 10⁻⁵ m** (eller 30 μm).

---

## Opgave 4: NTC resistor

![Opgave 4 Image 1](images/image_5.png)
![Opgave 4 Image 2](images/image_6.png)

**a) Beregn den effekt, hvormed der omsættes elektrisk energi i NTC resistoren.**

*   **Goal:** Calculate the power (P) dissipated in the NTC resistor under the specified conditions.
*   **Knowns:**
    *   Resistance of NTC resistor, R_NTC = 25 kΩ = 25 * 10³ Ω.
    *   Current through NTC resistor, I = 1.9 mA = 1.9 * 10⁻³ A.
*   **Formula:** Power dissipated in a resistor can be calculated using:
    ```
    P = I² * R
    ```
    (Alternatively, P = V * I or P = V² / R could be used if the voltage across the resistor was known).
*   **Calculation:**
    ```
    P_NTC = I² * R_NTC
    P_NTC = (1.9 * 10⁻³ A)² * (25 * 10³ Ω)
    P_NTC = (3.61 * 10⁻⁶ A²) * (25 * 10³ Ω)
    P_NTC = 0.09025 W
    ```
*   **Significant Figures:** Both I and R_NTC are given with two significant figures. The result should be rounded to two significant figures.
    ```
    P_NTC ≈ 0.090 W
    ```
    This can also be expressed as 90 mW (milliwatts).
*   **Answer:** Effekten, hvormed der omsættes elektrisk energi i NTC resistoren, er **0.090 W** (eller 90 mW).

**b) Bestem NTC resistorens temperatur.**

*   **Goal:** Determine the temperature (T) of the NTC resistor when the voltage across it is 3.5 V.
*   **Knowns:**
    *   Circuit diagram: A voltage source U = 12.0 V is connected in series with a fixed resistor R = 31 kΩ and the NTC resistor R_NTC.
    *   Voltage across the NTC resistor, U_NTC = 3.5 V.
    *   Graph relating the resistance of the NTC resistor (R_NTC) to its temperature (T).
*   **Method:**
    1.  Calculate the resistance of the NTC resistor (R_NTC) using the circuit information.
    2.  Use the provided graph to find the temperature corresponding to this resistance.
*   **Step 1: Calculate R_NTC**
    *   Since R and R_NTC are in series, the total voltage U is divided between them: U = U_R + U_NTC.
    *   Find the voltage across the fixed resistor R:
        ```
        U_R = U - U_NTC = 12.0 V - 3.5 V = 8.5 V
        ```
    *   The current (I) is the same through both resistors in a series circuit. Calculate the current using Ohm's law for resistor R:
        ```
        I = U_R / R = 8.5 V / (31 * 10³ Ω) ≈ 0.00027419 A (or 0.27419 mA)
        ```
    *   Now, calculate the resistance of the NTC resistor using Ohm's law for R_NTC:
        ```
        R_NTC = U_NTC / I = 3.5 V / 0.00027419 A ≈ 12765 Ω
        ```
    *   Convert to kΩ for easier graph reading:
        ```
        R_NTC ≈ 12.8 kΩ
        ```
*   **Step 2: Read Temperature from Graph**
    *   Locate R_NTC ≈ 12.8 kΩ on the vertical axis (R_NTC / kΩ) of the graph (image_6.png).
    *   Follow this value horizontally across to intersect the curve.
    *   From the intersection point, drop vertically down to read the corresponding temperature on the horizontal axis (T / °C).
    *   Reading the graph: 12.8 kΩ lies between 10 kΩ and 15 kΩ. Following the 12.8 kΩ level across, it intersects the curve roughly above 31°C. (e.g., 10 kΩ ≈ 36°C, 15 kΩ ≈ 27°C. 12.8 kΩ is closer to 15 than 10, so the temperature should be closer to 27°C than 36°C). Let's refine: it looks very close to T = 31 °C.
*   **Significant Figures:** Voltages have 2 or 3 sig figs. R has 2. The calculated R_NTC is roughly 12.8 kΩ (3 sig figs). Reading the graph introduces uncertainty. Let's estimate the temperature to the nearest degree.
*   **Answer:** NTC resistorens modstand er beregnet til ca. 12.8 kΩ. Aflæsning på grafen viser, at dette svarer til en temperatur på ca. **31 °C**.

---

## Opgave 5: E-cigaret (E-cigarette)

![Opgave 5 Image](images/image_7.png)

**a) Bestem, hvor lang tid der i alt kan suges på e-cigaretten, før batteriet skal genoplades.**

*   **Goal:** Calculate the total time (t) the e-cigarette can be used before the battery needs recharging.
*   **Knowns:**
    *   Battery voltage (Spændingsfald), U = 3.7 V (assumed constant).
    *   Power consumption during use (effekt), P = 5.5 W.
    *   Battery capacity (ladning), Q = 5.04 kC = 5040 C.
*   **Method 1: Using Energy**
    *   Total energy stored in the battery, E_total = Q * U (assuming constant voltage).
    *   Energy is consumed at a rate P (Power = Energy/time).
    *   Time t = E_total / P.
    *   Formula:
        ```
        t = (Q * U) / P
        ```
*   **Method 2: Using Current**
    *   Calculate the current drawn from the battery: P = U * I => I = P / U.
    *   Calculate the time using the definition of charge: Q = I * t => t = Q / I.
    *   Formula:
        ```
        t = Q / (P / U) = (Q * U) / P
        ```
    *(Both methods lead to the same formula)*
*   **Calculation:**
    ```
    t = (5040 C * 3.7 V) / 5.5 W
    t = 18648 J / 5.5 J/s
    t ≈ 3390.5 s
    ```
*   **Unit Conversion (Optional):** Convert seconds to minutes:
    ```
    t ≈ 3390.5 s / (60 s/min) ≈ 56.5 min
    ```
*   **Significant Figures:** U and P have 2 significant figures. Q has 3. The result should be rounded to 2 significant figures.
    ```
    t ≈ 3400 s
    ```
    or
    ```
    t ≈ 57 min
    ```
*   **Answer:** Der kan suges på e-cigaretten i alt i ca. **3400 sekunder** (eller ca. 57 minutter), før batteriet skal genoplades.

**b) Vurdér, hvor meget 1,2-propandiol e-cigaretten kan fordampe pr. sekund.**

*   **Goal:** Estimate the mass rate (ṁ) of 1,2-propanediol vaporization in grams per second (g/s).
*   **Knowns:**
    *   Power supplied, P = 5.5 W = 5.5 J/s.
    *   Data for 1,2-propanediol:
        *   Boiling point (Kogepunkt), T_boil = 187 °C.
        *   Specific heat capacity (Specifik varmekapacitet), c = 2.51 J/(g·K).
        *   Specific heat of vaporization (Specifik fordampningsvarme), L_v = 711 J/g.
*   **Assumptions:**
    *   The initial temperature of the 1,2-propanediol liquid (T_initial). A reasonable assumption is room temperature, e.g., T_initial = 20 °C.
    *   All the supplied power (5.5 W) goes into heating and vaporizing the liquid, with no heat loss.
*   **Method:**
    1.  Calculate the energy required to heat 1 gram of the liquid from T_initial to T_boil (Q_heat).
    2.  Calculate the energy required to vaporize 1 gram of the liquid at T_boil (Q_vap).
    3.  Calculate the total energy required per gram (Q_total_per_gram).
    4.  Determine the mass rate by dividing the power supplied by the energy required per gram.
*   **Formula:**
    *   Q_heat = c * ΔT = c * (T_boil - T_initial)
    *   Q_vap = L_v
    *   Q_total_per_gram = Q_heat + Q_vap
    *   Mass rate, ṁ = P / Q_total_per_gram
*   **Calculation:**
    *   Temperature change, ΔT = 187 °C - 20 °C = 167 °C = 167 K (change in °C is equal to change in K).
    *   Energy to heat 1 gram:
        ```
        Q_heat = (2.51 J/(g·K)) * (167 K) ≈ 419.17 J/g
        ```
    *   Energy to vaporize 1 gram:
        ```
        Q_vap = 711 J/g
        ```
    *   Total energy per gram:
        ```
        Q_total_per_gram = 419.17 J/g + 711 J/g ≈ 1130.17 J/g
        ```
    *   Mass vaporization rate:
        ```
        ṁ = P / Q_total_per_gram = (5.5 J/s) / (1130.17 J/g)
        ṁ ≈ 0.004866 g/s
        ```
*   **Significant Figures:** Power P has 2 sig figs. Heat capacities and boiling point have 3. The assumed initial temperature influences the result slightly. Rounding to 2 significant figures based on the power seems appropriate.
    ```
    ṁ ≈ 0.0049 g/s
    ```
    This can also be expressed as 4.9 mg/s (milligrams per second).
*   **Answer:** E-cigaretten kan fordampe ca. **0.0049 gram 1,2-propandiol pr. sekund** (eller 4.9 mg/s), under antagelse af en starttemperatur på 20 °C og ingen varmetab.

---

## Opgave 6: Alcator C-Mod (Tokamak)

![Opgave 6 Image](images/image_9.png)

**a) Bestem størrelsen af det maksimale magnetfelt midt i torussen.**

*   **Goal:** Calculate the magnitude of the maximum magnetic field (B) in the center of the torus (at the major radius).
*   **Knowns:**
    *   Major radius, R = 0.67 m.
    *   Number of windings (toroidal field coils), N = 120.
    *   Maximum current in the windings, I_winding = 250 kA = 250 * 10³ A. (Assuming this is current per winding).
    *   Permeability of free space, μ₀ = 4π * 10⁻⁷ T·m/A.
*   **Formula:** The toroidal magnetic field near the center of a tokamak (approximating it as a toroidal solenoid) at the major radius R is given by:
    ```
    B ≈ (μ₀ * N * I_winding) / (2 * π * R)
    ```
    This formula calculates the field generated by the current flowing in the toroidal direction through the N windings.
*   **Calculation:**
    ```
    B ≈ ( (4π * 10⁻⁷ T·m/A) * 120 * (250 * 10³ A) ) / ( 2 * π * 0.67 m )
    ```
    Simplify by cancelling 2π:
    ```
    B ≈ ( (2 * 10⁻⁷ T·m/A) * 120 * (2.5 * 10⁵ A) ) / ( 0.67 m )
    B ≈ ( (2 * 10⁻⁷) * (120 * 2.5 * 10⁵) ) / 0.67 T
    B ≈ ( (2 * 10⁻⁷) * (3 * 10⁷) ) / 0.67 T
    B ≈ ( 6 ) / 0.67 T
    B ≈ 8.955 T
    ```
*   **Significant Figures:** R has 2 sig figs, N is exact, I_winding has 3 sig figs. The result should be rounded to 2 significant figures.
    ```
    B ≈ 9.0 T
    ```
*   **Answer:** Størrelsen af det maksimale magnetfelt midt i torussen er ca. **9.0 T**.

**b) Bestem tætheden af deuterium i plasmaet.**

*   **Goal:** Calculate the number density (tæthed, n_D) of deuterium ions in the plasma.
*   **Knowns:**
    *   Plasma constituents: Deuterium (D, ²H) and Helium-3 (³He).
    *   Densities are equal: n_D = n_He.
    *   Plasma temperature, T = 58 MK = 58 * 10⁶ K.
    *   Measured D-³He fusion reaction rate, R_rate = 6.4 * 10¹² m⁻³·s⁻¹.
    *   Graph showing Reactivity (<σv>) vs. Temperature (T) for the D + ³He → ⁴He + p fusion reaction. The reactivity is plotted as Reactivity / (10⁻²⁷ m³/s).
*   **Formula:** The reaction rate for fusion between two species (D and ³He here) is given by:
    ```
    R_rate = n_D * n_He * <σv>
    ```
    Since n_D = n_He, this becomes:
    ```
    R_rate = n_D² * <σv>
    ```
    where <σv> is the reactivity parameter, which depends on temperature.
*   **Method:**
    1.  Read the reactivity <σv> from the graph at T = 58 MK.
    2.  Solve the rate equation for n_D.
*   **Step 1: Read Reactivity <σv> from Graph**
    *   Locate T = 58 MK on the horizontal axis (T/MK). This is between 50 and 100.
    *   Go vertically up to the plotted line.
    *   Read the corresponding value on the vertical axis (Reaktivitet / 10⁻²⁷ m³/s). The vertical axis is logarithmic.
    *   At T=50 MK, the value is 10 (x 10⁻²⁷ m³/s).
    *   At T=100 MK, the value is about 90 (x 10⁻²⁷ m³/s).
    *   At T=58 MK, the value is between 10 and 90. Since the y-axis is logarithmic, we need to be careful. 58 is much closer to 50 than 100. Let's estimate by eye or interpolate on the log scale. It looks like the value is around 14-15 on the vertical axis scale.
    *   Let's try the log interpolation used in the thought process: T=50 -> Y=10; T=100 -> Y=90. We want Y at T=58.
        log(Y) = log(10) + (log(90)-log(10))/(100-50) * (58-50)
        log(Y) = 1 + (log(9)/50) * 8
        log(Y) ≈ 1 + (0.954/50) * 8 ≈ 1 + 0.019 * 8 ≈ 1 + 0.152 = 1.152
        Y = 10^1.152 ≈ 14.19
    *   So, the Reactivity value on the axis is ≈ 14.2.
    *   Therefore, the reactivity is:
        ```
        <σv> ≈ 14.2 * 10⁻²⁷ m³/s
        ```
*   **Step 2: Calculate n_D**
    *   Rearrange the rate equation:
        ```
        n_D² = R_rate / <σv>
        ```
    *   Substitute values:
        ```
        n_D² = (6.4 * 10¹² m⁻³·s⁻¹) / (14.2 * 10⁻²⁷ m³/s)
        n_D² ≈ 4.507 * 10³⁸ m⁻⁶
        ```
    *   Take the square root:
        ```
        n_D = √(4.507 * 10³⁸ m⁻⁶) ≈ 2.123 * 10¹⁹ m⁻³
        ```
*   **Significant Figures:** R_rate has 2 sig figs, T has 2 sig figs. The value read from the graph (<σv>) might have 2 or 3. Let's round the final answer to 2 significant figures.
    ```
    n_D ≈ 2.1 * 10¹⁹ m⁻³
    ```
*   **Answer:** Tætheden af deuterium i plasmaet er ca. **2.1 x 10¹⁹ m⁻³**.

---

## Opgave 7: Curiosity (Mars Lander)

![Opgave 7 Image](images/image_10.png)

**a) Hvor lang tid tog den sidste fase af landingen?**

*   **Goal:** Calculate the time duration (t) of the final phase of landing.
*   **Knowns:**
    *   Distance covered in the final phase, Δy = 20 m.
    *   Constant velocity during this phase, v = 0.60 m/s.
*   **Formula:** For motion with constant velocity, distance = velocity × time:
    ```
    Δy = v * t
    ```
*   **Derivation:** Solve for time t:
    ```
    t = Δy / v
    ```
*   **Calculation:**
    ```
    t = 20 m / 0.60 m/s
    t ≈ 33.33 s
    ```
*   **Significant Figures:** Δy has 2 sig figs (implied by 20), v has 2 sig figs. Round the result to 2 significant figures.
    ```
    t ≈ 33 s
    ```
*   **Answer:** Den sidste fase af landingen tog ca. **33 sekunder**.

**b) Bestem rumsondens tab i mekanisk energi fra højden 125 km til højden 1,5 km.**

*   **Goal:** Calculate the loss in mechanical energy (ΔE_mech) of the lander between two altitudes.
*   **Knowns:**
    *   Initial height, h_i = 125 km = 125000 m.
    *   Final height, h_f = 1.5 km = 1500 m.
    *   Initial speed, v_i = 5.9 * 10³ m/s.
    *   Final speed, v_f = 79 m/s.
    *   Lander mass, m = 3.3 * 10³ kg.
    *   Acceleration due to gravity on Mars, g_mars = 3.72 m/s².
*   **Formula:** Mechanical energy is the sum of kinetic energy (K) and potential energy (U).
    *   K = (1/2) * m * v²
    *   U = m * g * h (assuming g is constant over the altitude change, a reasonable approximation here).
    *   Change in mechanical energy, ΔE_mech = E_mech_final - E_mech_initial
    *   ΔE_mech = (K_f + U_f) - (K_i + U_i)
    *   ΔE_mech = ( (1/2)mv_f² + mgh_f ) - ( (1/2)mv_i² + mgh_i )
    *   ΔE_mech = (1/2)m(v_f² - v_i²) + mg(h_f - h_i)
*   **Calculation:**
    *   Change in kinetic energy term:
        ```
        ΔK = (1/2) * (3.3 * 10³ kg) * [ (79 m/s)² - (5.9 * 10³ m/s)² ]
        ΔK = (1.65 * 10³ kg) * [ 6241 m²/s² - 3.481 * 10⁷ m²/s² ]
        ΔK ≈ (1.65 * 10³ kg) * [ -3.480 * 10⁷ m²/s² ]
        ΔK ≈ -5.743 * 10¹⁰ J
        ```
    *   Change in potential energy term:
        ```
        ΔU = (3.3 * 10³ kg) * (3.72 m/s²) * (1500 m - 125000 m)
        ΔU = (12276 N) * (-123500 m)
        ΔU ≈ -1.516 * 10⁹ J
        ```
    *   Total change in mechanical energy:
        ```
        ΔE_mech = ΔK + ΔU ≈ (-5.743 * 10¹⁰ J) + (-0.1516 * 10¹⁰ J)
        ΔE_mech ≈ -5.895 * 10¹⁰ J
        ```
*   **Loss of Energy:** The loss in mechanical energy is the negative of the change (since the change is negative).
    ```
    Loss = - ΔE_mech ≈ 5.895 * 10¹⁰ J
    ```
*   **Significant Figures:** Speeds have 2 sig figs. Mass has 2 sig figs. Gravity has 3 sig figs. Heights have 2 or 3. The result should be rounded to 2 significant figures.
    ```
    Loss ≈ 5.9 * 10¹⁰ J
    ```
*   **Answer:** Rumsondens tab i mekanisk energi er ca. **5.9 x 10¹⁰ J**.

**c) Bestem størrelsen af rumsondens acceleration i højden 1,5 km.**

*   **Goal:** Calculate the magnitude of the lander's acceleration (a) at h = 1.5 km.
*   **Knowns:**
    *   Altitude, h = 1.5 km.
    *   Speed at this altitude, v = 79 m/s.
    *   Parachute diameter, D = 21.35 m.
    *   Atmospheric density at this altitude, ρ_atm = 0.020 kg/m³.
    *   Drag coefficient of parachute, C_d = 0.66.
    *   Lander mass, m = 3.3 * 10³ kg.
    *   Mars gravity, g_mars = 3.72 m/s².
*   **Forces:** Two main forces act on the lander:
    *   Gravity (downward): F_g = m * g_mars
    *   Aerodynamic Drag (upward, opposing motion): F_d = (1/2) * ρ_atm * v² * A * C_d
*   **Newton's Second Law:** The net force determines the acceleration:
    ```
    F_net = ΣF = m * a
    ```
    Let's define the downward direction as positive. Then:
    ```
    F_net = F_g - F_d
    m * a = m * g_mars - (1/2) * ρ_atm * v² * A * C_d
    ```
*   **Calculations:**
    *   Calculate parachute area (A), assuming it's circular:
        *   Radius, r = D / 2 = 21.35 m / 2 = 10.675 m.
        *   Area, A = π * r² = π * (10.675 m)² ≈ 358.0 m².
    *   Calculate gravitational force:
        ```
        F_g = (3.3 * 10³ kg) * (3.72 m/s²) = 12276 N
        ```
    *   Calculate drag force:
        ```
        F_d = 0.5 * (0.020 kg/m³) * (79 m/s)² * (358.0 m²) * 0.66
        F_d = 0.5 * 0.020 * 6241 * 358.0 * 0.66
        F_d ≈ 14780 N
        ```
    *   Calculate net force:
        ```
        F_net = F_g - F_d = 12276 N - 14780 N = -2504 N
        ```
        (The negative sign indicates the net force is upward, causing deceleration).
    *   Calculate acceleration:
        ```
        a = F_net / m = -2504 N / (3.3 * 10³ kg)
        a ≈ -0.7588 m/s²
        ```
*   **Magnitude:** The question asks for the *size* (størrelsen) of the acceleration, which is the absolute value.
    ```
    |a| ≈ 0.7588 m/s²
    ```
*   **Significant Figures:** Density has 2 sig figs, speed has 2, mass has 2, Cd has 2, g has 3, diameter has 4. The result should be limited by the least precise values, likely 2 significant figures.
    ```
    |a| ≈ 0.76 m/s²
    ```
*   **Answer:** Størrelsen af rumsondens acceleration i højden 1,5 km er ca. **0.76 m/s²**.

---

## Opgave 8: Hot Stone massage

![Opgave 8 Image](images/image_11.png)

**a) Bestem varmelegemets resistans, når spændingsfaldet over varmelegemet er 230 V.**

*   **Goal:** Calculate the resistance (R) of the heating element.
*   **Knowns:**
    *   Power of the heating element, P = 1.20 kW = 1200 W.
    *   Voltage across the heating element, U = 230 V.
*   **Formula:** The relationship between power (P), voltage (U), and resistance (R) is given by:
    ```
    P = U² / R
    ```
*   **Derivation:** Solve for resistance R:
    ```
    R = U² / P
    ```
*   **Calculation:**
    ```
    R = (230 V)² / 1200 W
    R = 52900 V² / 1200 W
    R ≈ 44.083 Ω
    ```
*   **Significant Figures:** Both P and U are given with 3 significant figures. Round the result to 3 significant figures.
    ```
    R ≈ 44.1 Ω
    ```
*   **Answer:** Varmelegemets resistans er ca. **44.1 Ω**.

**b) Vurdér, hvor lang tid der går, inden vandets og stenenes temperatur er 50 °C.**

*   **Goal:** Estimate the time (t) required to heat the water and stones to the target temperature.
*   **Knowns:**
    *   Volume of water, V_water = 9.0 L.
    *   Mass of stones, m_stones = 3.2 kg.
    *   Final temperature, T_final = 50 °C.
    *   Specific heat capacity of stones, c_stones = 920 J/(kg·K).
    *   Power input from heater, P = 1.20 kW = 1200 W = 1200 J/s.
*   **Needed Values & Assumptions:**
    *   Mass of water: Density of water ≈ 1.0 kg/L. So, m_water = 9.0 L * 1.0 kg/L = 9.0 kg.
    *   Specific heat capacity of water: c_water ≈ 4186 J/(kg·K) (standard value).
    *   Initial temperature (T_initial): Assume a typical starting room temperature, e.g., T_initial = 20 °C.
    *   Assumption: No heat is lost to the surroundings; all heater energy goes into the water and stones.
*   **Formula:**
    *   The total heat energy (Q_total) required is the sum of the heat needed for the water (Q_water) and the stones (Q_stones).
        ```
        Q_total = Q_water + Q_stones
        ```
    *   Heat required for each component: Q = m * c * ΔT, where ΔT = T_final - T_initial.
    *   Energy supplied by the heater in time t: E_supplied = P * t.
    *   Assuming E_supplied = Q_total:
        ```
        P * t = (m_water * c_water * ΔT) + (m_stones * c_stones * ΔT)
        P * t = (m_water * c_water + m_stones * c_stones) * ΔT
        ```
*   **Derivation:** Solve for time t:
    ```
    t = [ (m_water * c_water + m_stones * c_stones) * ΔT ] / P
    ```
*   **Calculation:**
    *   Temperature change: ΔT = 50 °C - 20 °C = 30 °C = 30 K.
    *   Calculate terms inside the bracket:
        *   m_water * c_water = (9.0 kg) * (4186 J/(kg·K)) = 37674 J/K.
        *   m_stones * c_stones = (3.2 kg) * (920 J/(kg·K)) = 2944 J/K.
        *   Sum = 37674 J/K + 2944 J/K = 40618 J/K.
    *   Calculate total heat required:
        ```
        Q_total = (40618 J/K) * (30 K) = 1218540 J
        ```
    *   Calculate time:
        ```
        t = Q_total / P = 1218540 J / (1200 J/s)
        t ≈ 1015.45 s
        ```
*   **Unit Conversion (Optional):** Convert seconds to minutes:
    ```
    t ≈ 1015.45 s / (60 s/min) ≈ 16.9 min
    ```
*   **Significant Figures:** Masses and power have 2 or 3 sig figs. Specific heats have 3 or 4. Temperatures might be considered exact or have 2 sig figs for the difference. Let's round to 2 significant figures based on the masses.
    ```
    t ≈ 1000 s
    ```
    or
    ```
    t ≈ 17 min
    ```
*   **Answer:** Det tager ca. **1000 sekunder** (eller ca. 17 minutter) at opvarme vandet og stenene til 50 °C, under antagelse af en starttemperatur på 20 °C og intet varmetab.

---

## Opgave 9: Antennagalaksen (Antennae Galaxies)

![Opgave 9 Image](images/image_12.png)

**a) Bestem den største bølgelængde af den stråling, som Chandra-teleskopet måler.**

*   **Goal:** Find the longest wavelength (λ_max) corresponding to the detected photon energies.
*   **Knowns:**
    *   Detected photon energies: E₁ = 1.6 * 10⁻¹⁷ J and E₂ = 1.6 * 10⁻¹⁵ J.
    *   Planck's constant, h ≈ 6.626 * 10⁻³⁴ J·s.
    *   Speed of light, c ≈ 3.00 * 10⁸ m/s.
*   **Formula:** The energy (E) of a photon is related to its wavelength (λ) by:
    ```
    E = h * f = h * (c / λ)
    ```
*   **Relationship:** Energy and wavelength are inversely proportional (E ∝ 1/λ). Therefore, the longest wavelength (λ_max) corresponds to the *lowest* photon energy (E_min).
*   **Identify Minimum Energy:**
    ```
    E_min = 1.6 * 10⁻¹⁷ J
    ```
*   **Derivation:** Solve the energy formula for λ:
    ```
    λ = h * c / E
    ```
*   **Calculation:** Calculate λ_max using E_min:
    ```
    λ_max = (h * c) / E_min
    λ_max = (6.626 * 10⁻³⁴ J·s * 3.00 * 10⁸ m/s) / (1.6 * 10⁻¹⁷ J)
    λ_max ≈ (1.9878 * 10⁻²⁵ J·m) / (1.6 * 10⁻¹⁷ J)
    λ_max ≈ 1.242 * 10⁻⁸ m
    ```
*   **Significant Figures:** Energies are given with 2 significant figures. h and c have more. Round the result to 2 significant figures.
    ```
    λ_max ≈ 1.2 * 10⁻⁸ m
    ```
    This can also be expressed as 12 nm (nanometers). This wavelength falls in the extreme ultraviolet / soft X-ray part of the spectrum.
*   **Answer:** Den største bølgelængde af den målte stråling er ca. **1.2 x 10⁻⁸ m** (eller 12 nm).

**b) Med hvilken fart bevæger Antennegalaksen sig væk fra os? Bestem afstanden til Antennegalaksen.**

*   **Goal:** Calculate the recessional velocity (v) and the distance (d) to the Antennae Galaxies.
*   **Knowns:**
    *   Redshift, z = 0.005688.
    *   Speed of light, c ≈ 3.00 * 10⁸ m/s.
*   **Needed Value:** Hubble constant (H₀). A commonly used approximate value is H₀ ≈ 70 km/s/Mpc (kilometers per second per Megaparsec).
*   **Formula (Velocity):** For small redshifts (z << 1), the recessional velocity is approximately:
    ```
    v ≈ z * c
    ```
*   **Formula (Distance):** Hubble's Law relates velocity and distance:
    ```
    v = H₀ * d
    ```
*   **Calculation (Velocity):**
    ```
    v ≈ 0.005688 * (3.00 * 10⁸ m/s)
    v ≈ 1.7064 * 10⁶ m/s
    ```
    Convert to km/s:
    ```
    v ≈ 1706.4 km/s
    ```
*   **Calculation (Distance):**
    *   Rearrange Hubble's Law: d = v / H₀.
    *   Use consistent units (velocity in km/s, H₀ in km/s/Mpc).
    ```
    d ≈ (1706.4 km/s) / (70 km/s/Mpc)
    d ≈ 24.377 Mpc
    ```
*   **Significant Figures:** Redshift z has 4 significant figures. The approximate H₀ value (70) has only 2 significant figures, which limits the precision of the distance calculation. Velocity can be stated with 4 sig figs.
    ```
    v ≈ 1706 km/s
    d ≈ 24 Mpc
    ```
*   **Answer:** Antennegalaksen bevæger sig væk fra os med en fart på ca. **1706 km/s**. Afstanden til Antennegalaksen er ca. **24 Mpc** (Megaparsec), baseret på en Hubble-konstant på ca. 70 km/s/Mpc.

**c) Bestem Chandra-teleskopets fart, når det befinder sig længst væk fra Jorden.**

*   **Goal:** Calculate the speed of the Chandra telescope at its apogee (furthest point from Earth).
*   **Knowns:**
    *   Orbit is elliptical.
    *   Distance at perigee (closest), r_per = 2.26 * 10⁷ m (from Earth's center).
    *   Speed at perigee, v_per = 5.8 km/s = 5800 m/s.
    *   Distance at apogee (furthest), r_apo = 1.39 * 10⁸ m (from Earth's center).
*   **Principle:** Conservation of angular momentum for an object orbiting under a central force (like gravity).
*   **Formula:** Angular momentum L = m * r * v_perp, where v_perp is the velocity component perpendicular to the radius vector. At perigee and apogee, the velocity is entirely perpendicular to the radius vector. Conservation means L is constant:
    ```
    L_per = L_apo
    m * r_per * v_per = m * r_apo * v_apo
    ```
*   **Derivation:** The mass m cancels out. Solve for the speed at apogee (v_apo):
    ```
    v_apo = (r_per * v_per) / r_apo
    ```
*   **Calculation:**
    ```
    v_apo = ( (2.26 * 10⁷ m) * (5800 m/s) ) / (1.39 * 10⁸ m)
    v_apo = ( 1.3108 * 10¹¹ m²/s ) / (1.39 * 10⁸ m)
    v_apo ≈ 942.95 m/s
    ```
*   **Significant Figures:** Distances have 3 sig figs, v_per has 2 sig figs. The result should be rounded to 2 significant figures.
    ```
    v_apo ≈ 940 m/s
    ```
    or 0.94 km/s.
*   **Answer:** Chandra-teleskopets fart, når det er længst væk fra Jorden, er ca. **940 m/s** (eller 0.94 km/s).

---

## Opgave 10: Meget lille pacemaker (Tiny Pacemaker)

![Opgave 10 Image 1](images/image_13.png)
![Opgave 10 Image 2](images/image_14.png)

**a) Bestem spændingsfaldet over hjertet, når pacemakeren sender et elektrisk signal gennem hjertet.**

*   **Goal:** Calculate the voltage drop (U_heart) across the heart during a pacemaker pulse.
*   **Knowns:**
    *   Circuit diagram: Voltage source U = 6.5 V, internal resistance R = 450 Ω.
    *   Current during pulse, I = 8.9 mA = 8.9 * 10⁻³ A.
    *   The current flows through R and the heart tissue in series.
*   **Formula:** Kirchhoff's Voltage Law for the circuit loop: The sum of voltage drops equals the source voltage.
    ```
    U = U_R + U_heart
    ```
    where U_R is the voltage drop across the internal resistor. Using Ohm's Law:
    ```
    U_R = I * R
    ```
*   **Derivation:** Substitute U_R and solve for U_heart:
    ```
    U_heart = U - U_R = U - (I * R)
    ```
*   **Calculation:**
    ```
    U_R = (8.9 * 10⁻³ A) * (450 Ω) = 4.005 V
    U_heart = 6.5 V - 4.005 V = 2.495 V
    ```
*   **Significant Figures:** U has 2 sig figs, R has 2 sig figs, I has 2 sig figs. Round the result to 2 significant figures.
    ```
    U_heart ≈ 2.5 V
    ```
*   **Answer:** Spændingsfaldet over hjertet er ca. **2.5 V**, når pacemakeren sender et signal.

**b) Vurdér, hvor lang tid pacemakeren kan levere energi til hjertet.**

*   **Goal:** Estimate the operational lifetime (T_life) of the pacemaker.
*   **Knowns:**
    *   Energy delivered *to the heart* per pulse, E_pulse_heart = 3.5 μJ = 3.5 * 10⁻⁶ J. *(This interpretation is ambiguous, see below)*.
    *   Pulse duration, Δt_pulse = 0.50 ms = 0.50 * 10⁻³ s.
    *   Current during pulse, I = 8.9 mA = 8.9 * 10⁻³ A.
    *   Average heart rate, Rate = 74 beats/minute = 74 pulses/minute.
    *   Source voltage, U = 6.5 V.
*   **Missing Information & Ambiguity:** The total energy capacity (or charge capacity) of the pacemaker's battery is not provided. Furthermore, the statement "kan i alt levere energien 3.5 μJ til hjertet" is highly ambiguous. 3.5 μJ is far too small for total lifetime energy. It likely means energy *per pulse*. Does it mean energy *delivered to the heart* or energy *drawn from the battery* per pulse?
    *   **Interpretation 1:** 3.5 μJ is energy *drawn from battery* per pulse.
    *   **Interpretation 2:** 3.5 μJ is energy *delivered to heart* per pulse.
    *   **Interpretation 3 (Based on calculation):** Let's calculate the energy *drawn from the battery* per pulse using the source voltage, current, and duration.
        ```
        P_source = U * I = 6.5 V * 8.9 * 10⁻³ A = 0.05785 W
        E_pulse_drawn_calc = P_source * Δt_pulse = 0.05785 W * 0.50 * 10⁻³ s ≈ 2.89 * 10⁻⁵ J = 28.9 μJ
        ```
        This calculated value (29 μJ) is significantly different from the stated 3.5 μJ.
*   **Assumption:** To proceed, we must make assumptions.
    1.  Assume the 3.5 μJ refers to energy **drawn from the battery per pulse**. This uses the given value directly, though it contradicts our calculation.
    2.  Assume a **typical battery capacity** for a pacemaker. Modern pacemakers often use lithium-iodine batteries with capacities around 1-2 Ampere-hours (Ah). Let's assume a charge capacity Q_bat = 1.5 Ah and use the source voltage U=6.5V to estimate total energy.
        *   Q_bat = 1.5 Ah = 1.5 A * 3600 s = 5400 C.
        *   E_bat_total = Q_bat * U = 5400 C * 6.5 V = 35100 J. (This is a rough estimate).
*   **Method (Using Assumption 1 & 2):**
    1.  Calculate the average power consumption (P_avg) based on energy per pulse and pulse rate.
    2.  Calculate the lifetime by dividing the total estimated battery energy by the average power consumption.
*   **Calculation:**
    *   Energy consumed per minute:
        ```
        E_per_min = E_pulse_drawn * Rate
        E_per_min = (3.5 * 10⁻⁶ J/pulse) * (74 pulses/min) = 2.59 * 10⁻⁴ J/min
        ```
    *   Average power consumption:
        ```
        P_avg = E_per_min / (60 s/min)
        P_avg = (2.59 * 10⁻⁴ J/min) / (60 s/min) ≈ 4.317 * 10⁻⁶ W (or J/s)
        ```
    *   Estimate lifetime:
        ```
        T_life = E_bat_total / P_avg
        T_life ≈ 35100 J / (4.317 * 10⁻⁶ J/s) ≈ 8.13 * 10⁹ s
        ```
    *   Convert lifetime to years:
        ```
        T_life ≈ (8.13 * 10⁹ s) / (60 s/min * 60 min/hr * 24 hr/day * 365 days/year)
        T_life ≈ 258 years
        ```
*   **Discussion:** A lifetime of ~260 years seems unrealistically long for a pacemaker, suggesting either the assumed battery capacity is too high, or the stated energy per pulse (3.5 μJ) is too low if it represents energy drawn.
    *   If we use the *calculated* energy drawn per pulse (28.9 μJ):
        *   P_avg_calc = (28.9 * 10⁻⁶ J/pulse) * (74 pulses/min) / (60 s/min) ≈ 3.56 * 10⁻⁵ W.
        *   T_life_calc = 35100 J / (3.56 * 10⁻⁵ W) ≈ 9.86 * 10⁸ s ≈ 31 years.
    *   This value (~30 years) is much more consistent with modern long-life pacemakers. It suggests the 3.5 μJ value might be incorrect or misinterpreted, and using the calculated energy drawn (based on V, I, duration) is more plausible.
*   **Conclusion:** Due to ambiguity in the provided "3.5 μJ" value and the lack of battery capacity information, a precise answer is difficult. Estimating based on calculated energy drawn (29 μJ/pulse) and typical battery capacity (~35 kJ) yields a lifetime of roughly 30 years.
*   **Answer:** Vurderingen af pacemakerens levetid afhænger stærkt af fortolkningen af den angivne energi pr. puls og batteriets totale kapacitet, som ikke er opgivet. Hvis vi antager, at energiforbruget pr. puls er 3.5 μJ (som opgivet) og estimerer en total batterienergi på ca. 35 kJ, bliver levetiden urealistisk lang (>200 år). Hvis vi i stedet beregner energiforbruget pr. puls ud fra V, I og varighed til ca. 29 μJ, og bruger samme estimerede batterienergi, fås en levetid på ca. **30 år**, hvilket er mere realistisk for en moderne pacemaker. Derfor vurderes levetiden til at være i størrelsesordenen **årtier**, men en præcis beregning kræver flere oplysninger.
