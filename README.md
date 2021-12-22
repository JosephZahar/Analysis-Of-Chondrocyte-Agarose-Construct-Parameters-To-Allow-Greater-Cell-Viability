# Analysis-Of-Chondrocyte-Agarose-Construct-Parameters-To-Allow-Greater-Cell-Viability
<p align="justify">
The unique mechanical properties of the articular cartilage depend on the interactions between the chondrocytes and the Extracellular Matrix (ECM) that maintain the tissue. the main aim of this experiment is to determine the optimal in-vivo environment for chondrocytes to allow greater cell viability and gag concentration.
</p>

<p align="justify">
Chondrocytes specimens were isolated from a bovine metacarpal-phalangeal joint and seeded in both 4% and 6% agarose concentrations. The specimens were cultivated at Day 0 & 7 to test their mechanical properties (using stress-strain and stress relaxation) as well as their sGaG concentrations (using spectrophotometry). A one way ANOVA and Tukey’s honestly significantly differenced (HSD) were implemented to compare the results of the different constructs.
</p>

**Stress-Strain graphs for each specimen of different agarose constructs have been plotted in Figure 1 using Python.**

<p align="center">
  
![Stress - Strain](https://user-images.githubusercontent.com/70657426/147086309-cc255169-c0d7-4fd1-8466-eb8b1dac954e.png)
</p>

<p align="justify">
**The 15% Tangent Modulus was taken for each specimen.** 
The Mean and Standard Deviation were then calculated and were graphically presented using bar charts. A statistical comparison between the Mean Tangent Modulus of each construct was performed using a Boxplot
</p>

<p align="center">
  
![Figure_1](https://user-images.githubusercontent.com/70657426/147086751-079fce01-7804-4ba9-8c45-14d78a937bcd.png)
</p>

**The figure below graphically present the Mean and SD sGAG concentration calculated across the five samples using the DMB spectral method.**

<p align="center">
 <img src="https://user-images.githubusercontent.com/70657426/147086837-e1b57483-a2f9-4ded-aced-ba299f3065e9.png"  width="600" height="600" />

</p>


<p align="justify">
A One-Way ANOVA was used to compare the sGAG concentration means of 4 constructs presented in Table 1 below. It was shown that there was significant difference between all the groups (p-value highlighted in green <0.05). However, ANOVA does not tell which constructs are significantly different from each other. To find out, we will perform post hoc comparison analysis for all unplanned comparison using Tukey’s honestly significantly differenced (HSD) test. ApartfromDay 0–4%agarose & Day 0–6% agarose with a p-value equal to 0.9 > 0.05, There was a statistically significant difference between all other groups.
</p>
  
<p align="center">
<img width="751" alt="Screen Shot 2021-12-22 at 1 49 56 PM" src="https://user-images.githubusercontent.com/70657426/147088537-fb9e3800-a126-4dad-a744-5cc2dded70ba.png">
</p>

<p align="justify">
ANOVA assumptions can be checked using visual approaches such as residual plots and histograms. As the standardized residuals lie around the 45-degree line, it suggests that the residuals are approximately normally distributed. In the histogram, the distribution looks approximately normal and suggests that residuals are approximately normally distributed
</p>

<p align="center">
<img width="986" alt="Screen Shot 2021-12-22 at 1 52 35 PM" src="https://user-images.githubusercontent.com/70657426/147088850-e68d64b9-163c-49c7-ba89-229f7b54d2f0.png">
</p>


