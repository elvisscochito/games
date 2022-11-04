using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Unity.MLAgents;
using Unity.MLAgents.Sensors;
using Unity.MLAgents.Actuators;

public class MyKartAgent : Agent
{
    public Transform sensors;
    public float speed = 1.0f;
    public float angularSpeed = 1.0f;
    float myHorizontal = 0; // front side
    Vector3 initialPosition;
    Quaternion initialRotation;

    // Start agent method
    public override void Initialize()
    {
        initialPosition = transform.position;
        initialRotation = transform.rotation;
    }

    // Actions to do when a training chapter begins
    public override void OnEpisodeBegin()
    {
        gameObject.transform.position = initialPosition;
        gameObject.transform.rotation = initialRotation;
        // begins with 0 velocity
        gameObject.GetComponent<Rigidbody>().velocity = Vector3.zero;
    }

    // Recolect observations and build the vector, to understand the enverioment 
    public override void CollectObservations(VectorSensor sensor)
    {
    }

    // Execute actions (from keyboard, learn module or previuos module)
    public override void OnActionReceived(ActionBuffers actions)
    {
    }

    // Control agent trought kerboard
    public override void Heuristic(in ActionBuffers actionsOut)
    {
    }
}
