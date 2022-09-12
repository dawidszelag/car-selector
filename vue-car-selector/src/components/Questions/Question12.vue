<template>
  <div>
    <question-label
        number="12"
        help-text="- select one"
        question="What boot capacity do you need?"/>
    <div class="answers-box">
      <radio-fields name="question12" keyValue="up_200" label="x- small - up to 200 L" @change="keyHandler"/>
      <radio-fields name="question12" keyValue="200" label="small - minimum 200 L" @change="keyHandler"/>
      <radio-fields name="question12" keyValue="300" label="medium - minimum 300 L" @change="keyHandler"/>
      <radio-fields name="question12" keyValue="500" label="large - minimum 500 L" @change="keyHandler"/>
      <radio-fields name="question12" keyValue="ute" label="ute open boot space" @change="keyHandler"/>
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
  if (key === 'up_200') {
    question.bootLte = 200;
    question.bootGte = null;
    question.bootUte = null;
  } else if (key === 'ute') {
    question.bootLte = null;
    question.bootGte = null;
    question.bootUte = true;
  } else if (key === '0') {
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
