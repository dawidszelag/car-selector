<template>
  <div>
    <question-label
        number="10"
        help-text="- select one"
        question="MINIMUM number of seats?"/>
    <div class="answers-box">
      <radio-fields name="question10" keyValue="2" label="2 seats" @change="keyHandler"/>
      <radio-fields name="question10" keyValue="4" label="4 seats" @change="keyHandler"/>
      <radio-fields name="question10" keyValue="5" label="5 seats" @change="keyHandler"/>
      <radio-fields name="question10" keyValue="7" label="7 seats" @change="keyHandler"/>
      <radio-fields name="question10" keyValue="8" label="8 seats" @change="keyHandler"/>
      <radio-fields name="question10" keyValue="9" label="9 seats" @change="keyHandler"/>
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
