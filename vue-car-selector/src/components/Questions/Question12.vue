<template>
  <div>
    <question-label
        number="12"
        help-text="- select one"
        question="MINIMUM boot space?"/>
    <div class="answers-box">
      <radio-fields name="question12" keyValue="120" label="1 suitcase – 120 litres" @change="keyHandler"/>
      <radio-fields name="question12" keyValue="240" label="2 suitcases - 240 litres" @change="keyHandler"/>
      <radio-fields name="question12" keyValue="360" label="3 suitcases - 360 litres" @change="keyHandler"/>
      <radio-fields name="question12" keyValue="480" label="4 suitcases - 480 litres" @change="keyHandler"/>
      <radio-fields name="question12" keyValue="600" label="5+ suitcases - 600 litres " @change="keyHandler"/>
      <radio-fields name="question12" keyValue="0" label="unsure" @change="keyHandler"/>
      <radio-fields name="question12" keyValue="0" label="doesn’t matter" @change="keyHandler"/>
    </div>
  </div>
</template>

<script setup>
import {reactive} from "vue";
import QuestionLabel from "../QuestionLabel";
import RadioFields from "../RadioFields";

const emit = defineEmits(['answers'])

const question = reactive({
  bootLte: null,
  bootGte: null,
  bootUte: null
})

const keyHandler = (key) => {
   if (key === '0') {
    question.bootLte = null;
    question.bootGte = null;
    question.bootUte = null;
  } else {
    question.bootLte = null;
    question.bootGte = parseInt(key);
    question.bootUte = null;
  }
  emit('answers', question)
}

</script>
