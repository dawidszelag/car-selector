<template>
  <div>
    <question-label
        number="14"
        help-text="- select one"
        question="Transmission?"/>
    <div class="answers-box">
      <radio-fields name="question14" keyValue="automatic" label="automatic" @change="keyHandler"/>
      <radio-fields name="question14" keyValue="manual" label="manual" @change="keyHandler"/>
      <radio-fields name="question14" keyValue="0" label="unsure" @change="keyHandler"/>
      <radio-fields name="question14" keyValue="0" label="doesn’t matter" @change="keyHandler"/>
    </div>
  </div>
</template>

<script setup>
import {reactive} from "vue";
import QuestionLabel from "../QuestionLabel";
import RadioFields from "../RadioFields";

const emit = defineEmits(['answers'])

const question = reactive({
  automatic: null,
  manual: null,
})

const keyHandler = (key) => {
  Object.keys(question).forEach(item => {
    if (key !== '0') {
      if (key === item) question[item] = true;
      else question[item] = null;
    }else {
      question[item] = null;
    }

  })

  emit('answers', question)
}

</script>
