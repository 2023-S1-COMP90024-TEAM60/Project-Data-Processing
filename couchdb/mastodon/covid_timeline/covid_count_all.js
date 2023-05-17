function(doc) {
    if (doc.content) {
      targets=['covid-19', 'covid', 'pandemic', 'coronarvirus', 'sars-cov-2', 'pfizer', 'moderna','quarantine','social distancing','pcr test','Vaccination','pcrtest', 'rat test', 'rattest']
      var pattern = RegExp("\\b(" + targets.join("|") + ")\\b", "gi");
      var matches = (doc.content || "").match(pattern) || [];
      var date=doc.created_at.split(" ")[0];
      if (matches.length > 0) {
        emit(date, 1);
      }
  }
  }

_sum