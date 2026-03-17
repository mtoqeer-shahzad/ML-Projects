export interface StudentData {
  gender: string;
  race_ethnicity: string;
  parental_level_of_education: string;
  lunch: string;
  test_preparation_course: string;
  reading_score: number;
  writing_score: number;
}

export interface PredictionResult {
  status: "success" | "failed";
  predicted_score?: number;
  error?: string;
}