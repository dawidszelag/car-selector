<template>
  <input
      class="field"
      :id="uniqueId"
      type="radio"
      :value="keyValue"
      :name="name"
      @input="$emit('change', keyValue)"
  />
  <label :for="uniqueId" class="option"> <span>{{ label }}</span></label>
</template>

<script setup>
import {defineProps, defineEmits} from "vue";
import {v4 as uuidv4} from "uuid";

const uniqueId = uuidv4();
defineEmits(['change'])
defineProps(['keyValue', 'label', 'name'])

</script>

<style scoped>

.field[type="radio"]:not(:checked),
.field[type="radio"]:checked {
  position: absolute;
  opacity: 0;
}


.field[type="radio"]:not(:checked) + label,
.field[type="radio"]:checked + label {
  position: relative;
  padding: 8.5px 15px;
  font-size: 15px;
  font-weight: 800;
  color: rgba(255, 255, 255, 0.85);
  cursor: pointer;
  background: rgba(0, 0, 0, 0.2);
  margin: 2px 0;
  margin-left: 30px;
  max-width: 350px;
  box-shadow: 0 2px 3px rgba(0, 0, 0, 0.4);
}

/* radio aspect */
.field[type="radio"]:not(:checked) + label:before,
.field[type="radio"]:checked + label:before {
  content: '';
  position: absolute;
  left: -42px;
  top: 0;
  width: 37px;
  height: 34px;
  background: rgba(0, 0, 0, 0.2);
  box-shadow: 0 2px 3px rgba(0, 0, 0, 0.4);
}

/* checked mark aspect */
.field[type="radio"]:not(:checked) + label:after,
.field[type="radio"]:checked + label:after {
  content: '✕';
  position: absolute;
  top: 18px;
  left: -28px;
  font-size: 12px;
  font-weight: 900;
  color: #fff;
  line-height: 0;
  transition: all .2s;
}


.field[type="radio"]:not(:checked) + label:hover,
.field[type="radio"]:not(:checked) + label:hover:before,
.field[type="radio"]:checked + label,
.field[type="radio"]:checked + label:after,
.field[type="radio"]:checked + label:before {
  background: rgba(255, 255, 255, 0.1);
}


.field[type="radio"]:checked + label:before {
  background: linear-gradient(#d71d80, #c42c8c) rgba(176, 30, 30, 0.3);
}

/* checked mark aspect changes */
.field[type="radio"]:not(:checked) + label:after {
  opacity: 0;
  transform: scale(0) rotate(45deg);
}

.field[type="radio"]:checked + label:after {
  opacity: 1;
  transform: scale(1) rotate(0);
}

/* Disabled radio */
.field[type="radio"]:disabled:not(:checked) + label:before,
.field[type="radio"]:disabled:checked + label:before {
  box-shadow: none;
  border-color: #bbb;
  background-color: #e9e9e9;
}

.field[type="radio"]:disabled:checked + label:after {
  color: #777;
}

.field[type="radio"]:disabled + label {
  color: #aaa;
}

/* End disabled radio */

</style>