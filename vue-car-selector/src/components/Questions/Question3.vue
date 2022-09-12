<template>
  <div>
    <question-label
        number="3"
        help-text="- select one"
        question="Where will you drive?"/>
    <div class="answers-box">
      <radio-fields name="question3" keyValue="shortDistance" label="Mainly local distance" @change="keyHandler"/>
      <radio-fields name="question3" keyValue="longDistance" label="Long distance" @change="keyHandler"/>
      <radio-fields name="question3" keyValue="mixedDistance" label="Mixed distance" @change="keyHandler"/>
      <radio-fields name="question3" keyValue="perfectCityCar" label="Perfect city car" @change="keyHandler"/>
    </div>
  </div>
</template>

<script setup>
import {reactive} from "vue";
import QuestionLabel from "../QuestionLabel";
import RadioFields from "../RadioFields";

const emit = defineEmits(['answers'])

const question = reactive({
  shortDistance: null,
  longDistance: null,
  mixedDistance: null,
  perfectCityCar: null,
})

const keyHandler = (key) => {
  Object.keys(question).forEach(item => {
    if (key === item) question[item] = true;
    else question[item] = null;
  })

  emit('answers', question)
}

</script>
