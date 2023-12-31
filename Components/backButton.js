import { View, Text, TouchableOpacity, Dimensions } from "react-native";
import React from "react";
import { ChevronLeftIcon } from "react-native-heroicons/outline";
import { useNavigation } from "@react-navigation/native";
import { Ionicons } from "@expo/vector-icons";
import { SafeAreaView } from "react-native-safe-area-context";

export default function BackButton() {
  const { width, height } = Dimensions.get("screen");
  const navigation=useNavigation();

  return (
    
    <TouchableOpacity onPress={() => navigation.goBack()}>
        <SafeAreaView
          style={{
            flexDirection: "row",
            alignItems: "center",
            width: 70,
            justifyContent: "center",
            // backgroundColor: "white",
            padding: 2,
            borderRadius: 10,

          }}
        >
          <Ionicons name="ios-arrow-back-outline" size={24} color="black" />
          <Text style={{ fontSize: 16, fontWeight: "600", marginLeft: 5 }}>
            Back
          </Text>
        </SafeAreaView>
      </TouchableOpacity>
  );
}
