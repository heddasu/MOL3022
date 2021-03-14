<template>
<div>
    <validation-observer ref="observer" v-slot="{ invalid }">
      <form @submit.prevent="submit">
        <v-container>
        <v-card elevation="2"
        class="my-5">
        <v-row>
          <v-card-title class="my-0 py-0">1. Enter DNA-sequence</v-card-title>
        </v-row>
        <v-row>
          <v-card-text class="my-0 py-0">A promotor sequence is mosed likely to give good results.</v-card-text>
        </v-row>
        <v-row>
          <v-card-text>
          <validation-provider
            v-slot="{ errors }"
            name="DNA-sequence"
            :rules= "{required: true,max:1000,min:20,regex:/^[!actgACTG]+$/}"
          >
            <v-text-field
              class="my-0 py-0"
              v-model="dnaSequence"
              :disabled="!editInput"
              :counter="1000"
              :error-messages="errors"
              color="black"
              label="DNA-sequence"
              required
            ></v-text-field>
          </validation-provider>
          </v-card-text>
        </v-row>
        </v-card>
        </v-container>
        <v-container>
        <v-card elevation="2"
        class="mb-10">
        <v-row>
          <v-card-title class="my-0 py-0">2. Choose motifs</v-card-title>
        </v-row>
        <v-row>
          <v-card-text class="my-0 py-0">
            The DNA-sequence is scanned, and among the chosen motifes, the most
            likely transcription factor binding sites in the sequence is
            identified.
          </v-card-text>
        </v-row>
        <v-row><v-card-text><validation-provider
          v-slot="{ errors }"
          name="Motifs"
          rules="required"
        >
        <v-autocomplete class="my-0 py-0"
            v-model="motifsChosen"
            color="black"
            :items="items"
            attach
            chips
            :disabled="!editInput"
            :error-messages="errors"
            label="Motifs"
            data-vv-name="select"
            required
            multiple
          ></v-autocomplete>
      </validation-provider></v-card-text>
        </v-row>
         </v-card>
           </v-container>
        <v-row 
        align="center"
        justify="space-around">
          <v-btn
            type="submit"
            v-if="revealButton"
            :disabled="invalid || loading"
            :loading="loading"
            elevation="2"
            rounded
            color="cyan"
            @click= "computeResults"
            >Compute result
          </v-btn>
        </v-row>
      </form>
    </validation-observer>
    <v-container>
        <v-card 
        v-if="revealResult"
        elevation="2"
        class="my-10">
        <v-row>
          <v-card-title class="my-0 py-0">Results</v-card-title>
        </v-row>
        <v-row>
          <v-card-text class="my-0 py-0">
            The DNA-sequence was scanned, and among the chosen motifes, the top 10 most
            likely transcription factor binding sites in the sequence was
            identified. Below is an illustration showing how the DNA-sequence is indexed in the result table. 
          </v-card-text>
          <v-card-text align="center" class="my-0 py-0">
            <v-img src="@/assets/Dna-sequence.png" max-width="700" ></v-img>
          </v-card-text>
        </v-row>
        <v-row>
          <v-card-text class="my-2 py-0">
            <h4>Chosen DNA-sequence: </h4>
            <p>{{dnaSequence}}</p>
          </v-card-text>
        </v-row>
        <v-row>
          <v-card-text class="my-2 py-0">
            <h4>Result:</h4>
            <ul>
            <li v-for="motif in results" :key="motif">{{motif}}</li>
            </ul>
          </v-card-text>
        </v-row>
            <v-row 
        align="center"
        justify="space-around">
          <v-btn
            class="my-2 py-0"
            elevation="2"
            rounded
            color="cyan"
            @click= "reset"
            >Reset
          </v-btn>
        </v-row>
        </v-card>
    </v-container>
  </div>
</template>

<script>
import { required, min, regex, max } from "vee-validate/dist/rules";
import {
  extend,
  ValidationObserver,
  ValidationProvider,
  setInteractionMode,
} from "vee-validate";
import axios from 'axios';

setInteractionMode("eager");

extend("required", {
  ...required,
  message: "{_field_} can not be empty",
});

extend("max", {
  ...max,
  message: "{_field_} may not be greater than {length} characters",
});

extend("min", {
  ...min,
  message: "{_field_} may not be less than {length} characters",
});

extend("regex", {
  ...regex,
  message: 
    "The {_field_} can only contain the characters A, T, C and G",
});

export default {
  components: {
    ValidationProvider,
    ValidationObserver,
  },
  props: {
  },
  data: () => ({
    dnaSequence: null,
    motifsChosen: [],
    select: null,
    loading: false,
    revealResult: false,
    revealButton: true,
    editInput: true,
    results: null,
    items: [],
  }),
  computed: {
  },
  methods: {
    getMotifs: function() {
      axios.get('http://127.0.0.1:8000/matrix/').then(
        response => {
          this.items = response.data.results.map(i => i.matrix_id)
        }
      );
    },
    postResults: function() {
      axios.post('http://127.0.0.1:8000/matrix/', {
        dnaSequence: this.dnaSequence, motifsChosen: this.motifsChosen}
        ).then(
        response => {
          this.results = response.data;
        }
      );
    
    },
    submit () {
      // Sjekker om form er fylt ut 
      this.$refs.observer.validate()
    },
    makeGraphs() {
      //"Result, sorted from most to least likely is presented below. Only the top X most likely binding sites are shown."
      //for x in this.results {
      //  "Motif id: " + i.matrix_id
      //  "Chance of attachment:" + i.matrix_score
      //}

      //TODO: 
      //Mulig å zoome i grafene
      //Y-aksen viser score for om det eksisterer et bindingssete for en gitt posisjon,
      //X-aksen viser hvilken posisjon det er snakk om.
    },
    computeResults () {
      //Sender valg til backend, går tilbake resultater, lager graf og viser dette til bruker. 
      this.loading = true
      
      this.postResults()

      this.makeGraphs()

      this.loading = false
      this.revealButton= false
      this.editInput = false
      this.revealResult= true
    }
  },
  reset () {
      //Reset alt / Starte applikasjon på nytt
      this.dnaSequence = null
      this.motifsChosen = []
      this.select = null
      this.revealResult = false
      this.revealButton = true
      this.editInput = true
      this.$refs.observer.reset()
    },
  beforeMount(){
    this.getMotifs()
 },
};
</script>

<style>
</style>