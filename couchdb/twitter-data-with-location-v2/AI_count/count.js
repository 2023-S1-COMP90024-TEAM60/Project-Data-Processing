function(doc) {
    if (doc.text) {
      targets=[' ai', 'Artificial Intelligence', 'Machine Learning','ML','Chatbots','nlp', 'AI ethics','Deep Learning','#ai', '#ArtificialIntelligence', '#MachineLearning','#ML','#Chatbots', '#nlp','#AIethics','#Robotics','#DeepLearning','#ComputerVision']
      var pattern = RegExp("\\b(" + targets.join("|") + ")\\b", "gi");
      var matches = (doc.text || "").match(pattern) || [];
      if (matches.length > 0) {
        emit([doc.state_code,doc.lga_code], 1);
      }
  }
  }

  _count