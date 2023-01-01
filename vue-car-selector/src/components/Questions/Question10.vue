<template>
  <div>
    <question-label
        number="10"
        help-text="- select one"
        question="What is the MINIMUM number of seats that you need?"/>
    <div class="answers-box">
      <radio-fields name="question10" keyValue="2" label="2" @change="keyHandler"/>
      <radio-fields name="question10" keyValue="4" label="4" @change="keyHandler"/>
      <radio-fields name="question10" keyValue="5" label="5" @change="keyHandler"/>
      <radio-fields name="question10" keyValue="7" label="7" @change="keyHandler"/>
      <radio-fields name="question10" keyValue="8" label="8" @change="keyHandler"/>
      <radio-fields name="question10" keyValue="9" label="9" @change="keyHandler"/>
    </div>
  </div>
</template>

<script setup>
import {reactive} from "vue";
import QuestionLabel from "../QuestionLabel";
import RadioFields from "../RadioFields";

const emit = defineEmits(['answers'])

const question = reactive({
  seats: null,
})

const keyHandler = (key) => {
  question.seats = parseInt(key)
  emit('answers', question)
}

</script>
