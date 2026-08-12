# Curriculum-Industry Skill Alignment Decision Framework Using Feast

## Student Details

**Name:** CHABOLU KASIM VALI

**Register Number:** 231FA04121

**Section:** CSE

---

## 1. Problem Statement

CSE graduates often possess academic knowledge but may lack the technical, practical, and professional skills expected by the IT industry.

This project identifies employability skill gaps by comparing student skill levels with industry skill requirements.

---

## 2. Dataset

The project uses a synthetic Curriculum-Industry Skill Alignment dataset.

**Total Students:** 5000

**Number of Employability Skills:** 7

### Skills

1. Programming
2. Database
3. Problem Solving
4. Communication
5. Cloud Computing
6. Teamwork
7. Aptitude

### Dataset Contains

- Student ID
- Branch
- Gender
- Student skill scores
- Industry skill requirements
- Individual skill gaps
- Skill Gap Category

### Target

`Skill Gap Category`

Categories:

- Low
- Medium
- High

The dataset entries were synthetically created for academic implementation.

---

## 3. Feature Engineering

The following reusable features were created:

| Feature | Meaning |
|---|---|
| technical_skill_avg | Average student score across seven employability skills |
| industry_requirement_avg | Average industry requirement across seven skills |
| calculated_skill_gap | Average skill gap across seven skills |
| requirement_difference | Difference between industry requirement and student skill |

### Feature Calculation

technical_skill_avg is calculated as the average of Programming, Database, Problem Solving, Communication, Cloud Computing, Teamwork and Aptitude.

requirement_difference is calculated as:

`industry_requirement_avg - technical_skill_avg`

---

## 4. Feast Architecture

```text
Original Dataset
       |
       v
Feature Engineering
       |
       v
Parquet Offline Data
       |
       v
Feast FeatureView
       |
       +----------------------+
       |                      |
       v                      v
Historical Features      Materialization
       |                      |
       v                      v
Model Training          Online Store
                              |
                              v
                       Online Retrieval
                              |
                              v
                          Prediction
```

---

## 5. Feast Implementation

### Entity

The Feast entity is `student`.

The entity join key is `student_id`.

### Data Source

The Feast data source is `skillgap_features.parquet`.

The timestamp field is `event_timestamp`.

### FeatureView

FeatureView name: `skillgap_features`

### Feature Service

`skillgap_prediction_service`

### Historical Retrieval

Historical features were retrieved using `get_historical_features()`.

### Machine Learning Model

A Random Forest Classifier was trained using Feast historical features.

### Online Retrieval

Online features were retrieved using `get_online_features()`.

---

## 6. Feast Registration

The Feast definitions were registered using:

`feast apply`

Registered objects:

- Entity: student
- FeatureView: skillgap_features
- Feature Service: skillgap_prediction_service

---

## 7. Offline Store

The offline store contains historical feature data.

It is used for:

- Historical feature retrieval
- Point-in-time feature generation
- Machine-learning training

---

## 8. Online Store

The online store contains materialized feature values.

It is used for:

- Fast feature retrieval
- Prediction-time feature access
- Consistent feature serving

---

## 9. Materialization

Materialization moves feature values from the offline data source into the online store.

---

## 10. Model Results

**Model:** Random Forest Classifier

**Model Accuracy:** 100.00%

**Historical Feature Output:** `results/historical_features.csv`

**Online Feature Output:** `results/online_features.csv`

**Selected Student:** CSE2610001

**Final Prediction:** Medium

---

## 11. Important Note About Model Accuracy

The model achieved 100.00% accuracy on the synthetic test dataset.

This result should not be interpreted as real-world performance because the dataset is synthetic and the target skill-gap category is strongly related to the skill-gap features used by the model.

Real industry data would be required to evaluate generalization to actual CSE graduates.

---

## 12. Limitations

1. The dataset is synthetic and may not completely represent real student skill levels.

2. Industry requirements may change over time, while the current dataset uses fixed requirements.

---

## 13. Future Improvements

1. Collect real curriculum and industry job-posting data.

2. Regularly update industry skill requirements.

3. Add placement and internship evidence.

4. Include employer feedback.

5. Add more industry-specific skills and certifications.

6. Use larger real-world datasets for model evaluation.

---

## 14. Conclusion

The project demonstrates a Curriculum-Industry Skill Alignment Decision Framework using Feast.

Student employability skills are compared with industry requirements to identify skill gaps.

Feast provides reusable feature management through entity creation, data source creation, FeatureView creation, historical feature retrieval, materialization and online feature retrieval.

The Random Forest model uses the retrieved Feast features to classify students into Low, Medium and High skill-gap categories.