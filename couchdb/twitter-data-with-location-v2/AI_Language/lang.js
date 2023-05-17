function(doc) {
    if (doc.lga_code && doc.lang&&doc.text) {
      targets=[' ai', 'Artificial Intelligence', 'Machine Learning','ML','Chatbots','nlp', 'AI ethics','Deep Learning','#ai', '#ArtificialIntelligence', '#MachineLearning','#ML','#Chatbots', '#nlp','#AIethics','#Robotics','#DeepLearning','#ComputerVision']
      var pattern = RegExp("\\b(" + targets.join("|") + ")\\b", "gi");
      var matches = (doc.text || "").match(pattern) || [];
      if (matches.length > 0) {
        if(doc.lang=='en'){
          emit([doc.state_code,doc.lga_code], {'en':1,'non_en':0,'tot':1});
        }
          emit([doc.state_code,doc.lga_code], {'en':0,'non_en':1,'tot':1});
    }
}
}

_sum