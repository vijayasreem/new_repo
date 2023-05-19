trigger LimitQuestionsPerSurvey on Survey_Question__c (before insert, before update) {
    if (Trigger.isBefore && (Trigger.isInsert || Trigger.isUpdate)) {
        Map<Id, Integer> surveyIdsToCount = new Map<Id, Integer>();

        for (Survey_Question__c q : Trigger.new) {
            if (surveyIdsToCount.containsKey(q.Survey__c)) {
                surveyIdsToCount.put(q.Survey__c, surveyIdsToCount.get(q.Survey__c) + 1);
            } else {
                surveyIdsToCount.put(q.Survey__c, 1);
            }
        }

        for (Survey_Question__c q : Trigger.new) {
            if (surveyIdsToCount.get(q.Survey__c) > 20) {
                q.addError('Cannot add more than 20 questions to one survey');
            }
        }
    }
}