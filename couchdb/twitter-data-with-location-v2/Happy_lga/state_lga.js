function(doc) {
    if (doc.sentiment && doc.created_at) {
      emit([doc.state_code,doc.lga_code], { sentiment_all: doc.sentiment, num: 1 });
    }
  }
_sum
