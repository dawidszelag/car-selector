<template>
  <div class="question-label">
    <div class="question-label__number">{{ number }}</div>
    <div class="question-label__text">{{ question }}
      <span>{{ helpText }}</span>
    </div>
  </div>
</template>

<script setup>
defineProps(['number', 'question', 'helpText'])
</script>

<style scoped>
.question-label {
  display: flex;
  align-items: center;
  width: 100%;
}

.question-label__text {
  display: block;
  font-size: 23px;
  font-weight: 700;
  color: #ffffff;
}

.question-label span {
  display: block;
  font-size: 15px;
}


.question-label__number {
  position: relative;
  display: flex;
  margin-top: -5px;
  justify-content: center;
  align-items: center;
  color: #fff;
  font-size: 20px;
  font-weight: 800;
  width: 60px;
  background: rgba(0, 0, 0, 0.2);
  margin-right: 20px;
  padding: 10px 0;
  box-shadow: 0 2px 3px rgba(0, 0, 0, 0.4);
}

.question-label__number:before {
  position: absolute;
  left: -12px;
  content: "";
  width: 8px;
  height: 100%;
  background: linear-gradient(#d71d80, #c42c8c) rgba(176, 30, 30, 0.3);
  box-shadow: 0 3px 4px rgba(0, 0, 0, 0.4);
}
</style>