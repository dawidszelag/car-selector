<template>
  <div class="content">
    <div class="box">
      <div class="box-title">
        <span>{{ question_number }}</span> of 17
      </div>
      <div class="box-content-questions">
          <Questions :question-number="question_number"/>
      </div>
      <div class="navigation" style="margin-right: 10px">
        <button
          class="button-back"
          v-on:click="question_number -= 1"
          v-if="question_number > 1"
        >
          Back
        </button>
        <button
          class="button-next"
          v-on:click="question_number += 1"
          v-if="question_number < 17"
        >
          Next
        </button>
        <button class="button-results" @click="showResults" v-if="question_number === 17">
          Show results
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import Questions from "@/components/Questions.vue";
import router from "@/router";
import store from "@/store";
export default {
  name: "Home",
  components: {
    Questions,
  },
  data: function () {
    return {
      question_number: 17,
    };
  },
  methods:{
    showResults: function (){
      store.state.page_number_models = 1;
      router.push({ name: 'models'})
    }
  }

};
</script>
<style scoped>
.content {
  background-color: rgba(0, 0, 0, 0.7);
  display: flex;
  align-items: flex-start;
  justify-content: center;
  padding-top: 200px;
  padding-bottom: 100px;
  min-height: 100vh;
  flex: 1;
}

.box {
  width: 80%;
  max-width: 650px;
}

.box-title {
  color: #ff005a;
  font-weight: 600;
  margin-bottom: 10px;
}

</style> 
