<template>
  <div class="content">
    <div class="box-info">
      <h1>
        LET'S GET <br />
        STARTED
      </h1>
      <p>Car Selector tool is here to help you with your car buying process.</p>
      <p>
        Make your search easier with Car Selector and find a vehicle that will
        perfectly suit your needs.
      </p>
      <p class="signature">by Anna Vinson</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "InfoBox",
};
</script>
<style scoped>
.content {
  display: flex;
  align-items: center;
  justify-content: center;
  padding-top: 100px;
  padding-bottom: 100px;
  min-height: 100vh;
  flex: 1;
  background-color: rgba(0, 0, 0, 0.5);
}

.box-info {
  padding: 35px;
  max-width: 500px;
  width: 95%;
}
.box-info h1 {
  font-size: 65px;
  font-weight: 700;
  line-height: 1.1;
}
.box-info p {
  font-size: 19px;
  font-weight: 600;
}
.box-info .signature {
  color: #ff005a;
  font-family: "Mr De Haviland", cursive;
  font-style: normal;
  font-size: 30px;
  letter-spacing: 3px;
}


</style>