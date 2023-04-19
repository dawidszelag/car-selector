<template>
  <div>
    <question-label
        number="9"
        help-text="- select one"
        question="How many doors?"/>
    <div class="answers-box">
      <RadioFields name="question9" keyValue="twoDoors" label="2 doors" @change="keyHandler"/>
      <RadioFields name="question9" keyValue="fourDoors" label="4 doors" @change="keyHandler"/>
      <RadioFields name="question9" keyValue="0" label="unsure" @change="keyHandler"/>
      <RadioFields name="question9" keyValue="0" label="doesn’t matter" @change="keyHandler"/>
    </div>
    <div>

    </div>
  </div>
</template>

<script setup>
import {reactive} from "vue";
import RadioFields from "../RadioFields";
import QuestionLabel from "../QuestionLabel";

const emit = defineEmits(['answers'])
const question = reactive({
  twoDoors: null,
  fourDoors: null,
  unsure: null,
  doesntMatter: null,
})

const keyHandler = (key) => {
  Object.keys(question).forEach(item => {
    if (key === item) question[item] = true;
    else question[item] = null;
  })

  emit('answers', question)
}

</script>
