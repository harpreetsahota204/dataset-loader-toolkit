datasets:
  text_vqa_subset:
    dataset_name: "lmms-lab/textvqa"
    split: "train"
    subset_size: 1000
    remove_cols:
      - "image_id"
      - "question_id"
      - "question_tokens"
      - "image_width"
      - "image_height"
      - "flickr_original_url"
      - "flickr_300k_url"
      - "image_classes"
      - "set_name"
      - "ocr_tokens"

  wild_vision:
    dataset_name: "WildVision/PublicBenchHub"
    split: "test"
    remove_cols:
      - "index"
      - "human_annotation"
      - "category"
      - "task_name"
    rename_cols:
      "gpt4_ha_answer": "answer"
      "image_input": "image"

  real_world_qa:
    dataset_name: "xai-org/RealworldQA"
    split: "test"

  m3_it_vqa_subset:
    dataset_name: "MMInstruction/M3IT"
    split: "train"
    subset_size: 1000
    remove_cols:
      - "inputs"
    rename_cols:
      "outputs": "answer"
      "instruction": "question"

  a_ok_vqa:
    dataset_name: "HuggingFaceM4/A-OKVQA"
    split: "train"
    subset_size: 1000
    remove_cols:
      - "question_id"
      - "direct_answers"
      - "difficult_direct_answer"
      - "rationales"

  doc_vqa:
    dataset_name: "lmms-lab/DocVQA"
    split: "train"
    subset_size: 1000
    remove_cols:
      - "questionId"
      - "question_types"
      - "ucsf_document_id"
      - "ucsf_document_page_no"
    data_dir: "DocVQA"

  info_graphic_vqa:
    dataset_name: "lmms-lab/DocVQA"
    split: "train"
    subset_size: 1000
    remove_cols:
      - "questionId"
      - "answer_type"
      - "image_url"
      - "operation/reasoning"
      - "ocr"
      - "data_split"
    data_dir: "InfographicVQA"