function(doc) {
    if (doc.lga_code && doc.lang&&doc.text) {
      targets=[' ai', 'Artificial Intelligence', 'Machine Learning','ML','Chatbots','nlp', 'AI ethics','Deep Learning','#ai', '#ArtificialIntelligence', '#MachineLearning','#ML','#Chatbots', '#nlp','#AIethics','#Robotics','#DeepLearning','#ComputerVision']
      var pattern = RegExp("\\b(" + targets.join("|") + ")\\b", "gi");
      var matches = (doc.text || "").match(pattern) || [];
      if (matches.length > 0) {
        var date = new Date(doc.created_at);
        emit([date.getUTCMonth(),doc.state_code,doc.lga_code], doc.sentiment);
    }
}
}
_stats