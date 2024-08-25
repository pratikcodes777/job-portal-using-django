def calculate_match_score(applicant_skills, job_required_skills):
    applicant_skills_set = set(applicant_skills.lower().split(","))
    job_required_skills_set = set(job_required_skills.lower().split(","))
    
    matching_skills = applicant_skills_set.intersection(job_required_skills_set)
    score = len(matching_skills) / len(job_required_skills_set) * 100 if job_required_skills_set else 0
    return score