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
            :rules= {required,max:1000,min:20}
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
            The DNA-sequence is scanned, and among the chosen motifes, the top 5 most
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
            :disabled="invalid"
            :loading="loading"
            elevation="2"
            rounded
            color="cyan"
            @click= "loader = 'loading'"
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
            The DNA-sequence was scanned, and among the chosen motifes, the top 5 most
            likely transcription factor binding sites in the sequence was
            identified. The results are shown as a graph.
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
            <h4>Chosen Motifs: </h4>
            <ul>
            <li v-for="motif in motifsChosen" :key="motif">{{motif}}</li>
            </ul>
          </v-card-text>
        </v-row>
        <v-row>
          <v-card-text class="my-2 py-0">
            <h4> Most likely transcription factor binding sites (sorted from most to least likely): </h4>
            <ul>
            <li v-for="motif in motifsResults" :key="motif">{{motif}}</li>
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
  ...regex, //TODO: Legg inn (v) => (v && !v.match("[^actgACTG]")) ||
  message: 
    "{_field_} {_value_} {regex} Sequence can only contain characters A, T, C and G",
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
    loader: null,
    loading: false,
    revealResult: false,
    revealButton: true,
    editInput: true,
    motifsResults: ["cat"], //TODO: Hent data fra database
    items: [ //TODO: Hent data fra database
        'MOTIF1',
        'MOTIF2',
        'MOTIF3',
        'MOTIF4',
    ],
  }),
  watch: {
      loader () {
        //Loader mens data sendes og motass 
        console.log("loaderdna = " + this.dnaSequenc)
        console.log("loadermotif = " + this.motifsChosen)
        //TODO: Send data
        const l = this.loader
        this[l] = !this[l]
        setTimeout(() => (this[l] = false), 3000) //TODO: Load til data er mottatt
        this.loader = null

        //TODO: if motatt data -> 
        if (this.loading == null) {
          this.presentResults()}
      }
  },
  computed: {
  },
  methods: {
    submit () {
      // Sjekker om form er fylt ut 
      this.$refs.observer.validate()
    },

    //async remove() {
    //  this.loading = true;
    //  await new Promise((resolve) => setTimeout(resolve, 3000)); //Oppdatere slik at den loader til resultater er klare
    //  this.loading = false;
    //},
  
    presentResults () {
      //Presentere resultatet
      
      //TODO: Fyll inn resultater + lag graf

      this.revealButton= false
      this.revealResult= true
      this.editInput = false
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
    }
  },
};
</script>

<style>
</style>