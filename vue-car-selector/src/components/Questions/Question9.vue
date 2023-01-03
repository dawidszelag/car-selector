<template>
  <div>
    <question-label
        number="9"
        help-text="- select all that apply"
        question="The number of doors that you need?"/>
    <div class="answers-box">
      <checkout-field v-model="question.twoDoors" label="2 doors"/>
      <checkout-field v-model="question.fourDoors" label="4 doors"/>
      <checkout-field v-model="question.unsure" label="unsure"/>
      <checkout-field v-model="question.doesntMatter" label="doesn’t matter"/>
    </div>
    <div>

    </div>
  </div>
</template>

<script setup>
import {reactive, watch} from "vue";
import QuestionLabel from "../QuestionLabel";
import CheckoutField from "../CheckboxField";

const emit = defineEmits(['answers'])
const question = reactive({
  twoDoors: null,
  fourDoors: null,
  unsure: null,
  doesntMatter: null,
})


watch(() => question.unsure, () => {
      if (question.unsure) {
        question.twoDoors = null;
        question.fourDoors = null;
        question.doesntMatter = null;
      }
    }
)

watch(() => question.doesntMatter, () => {
      if (question.doesntMatter) {
        question.twoDoors = null;
        question.fourDoors = null;
        question.unsure = null;
      }
    }
)

watch(() => [question.twoDoors, question.fourDoors], () => {
      if (question.twoDoors || question.fourDoors) {
        question.unsure = null;
        question.doesntMatter = null;
      }
      emit('answers', {
        twoDoors: question.twoDoors,
        fourDoors: question.fourDoors,
      })
    }
)
</script>
