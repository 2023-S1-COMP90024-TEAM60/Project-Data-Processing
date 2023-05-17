function (doc) {
    emit([doc.state_code,doc.lga_code],{'female':doc.female,'male':doc.male,'total_gender':doc.total_gender,
    'lang_en':doc.lang_en,'lang_other':doc.lang_other,'total_lang':doc.total_lang,
    'age_0_4':doc.age_0_4,'age_5_14':doc.age_5_14,'age_15_19':doc.age_15_19,
    'age_20_24':doc.age_20_24,'age_25_34':doc.age_25_34,'age_35_44':doc.age_35_44,
    'age_45_54':doc.age_45_54,'age_55_64':doc.age_55_64,'age_65_74':doc.age_65_74,
    'age_75_84':doc.age_75_84,'age_85ov':doc.age_85ov,'total_age':doc.total_age,
    'preschool':doc.preschool,'primary':doc.primary,'secondary':doc.secondary,
    'tertiary_vocational_edu':doc.tertiary_vocational_edu,'tertiary_uni_other_high':doc.tertiary_uni_other_high,
    'type_educanl_institution_not_stated':doc.type_educanl_institution_not_stated,'other_type_educ_instit':doc.other_type_educ_instit,
      'total_edu':doc.total_edu
    }
  );
  }

_sum